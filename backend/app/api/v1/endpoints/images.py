from fastapi import (
    APIRouter,
    Depends,
    File,
    HTTPException,
    UploadFile,
)

from fastapi.responses import RedirectResponse

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db

from app.crud.image import (
    create_image,
    delete_image,
    get_image_by_id,
    get_images_by_owner,
)

from app.models.image import Image
from app.models.user import User

from app.schemas.image import (
    ImageCreate,
    ImageResponse,
)

from app.services.ai import analyze_file

from app.services.s3 import (
    upload_file_to_s3,
    generate_presigned_url,
)

from app.utils.image_utils import extract_metadata

router = APIRouter(
    prefix="/images",
    tags=["Images"],
)

ALLOWED_TYPES = [

    # Images

    "image/jpeg",
    "image/png",
    "image/webp",
    "image/jpg",

    # Documents

    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",

    # Excel

    "application/vnd.ms-excel",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

    # CSV / TSV / Text

    "text/csv",
    "text/plain",
    "text/tab-separated-values",

    # Archives

    "application/zip",
    "application/x-zip-compressed",
    "application/x-rar-compressed",

    # Video

    "video/mp4",
    "video/quicktime",
    "video/x-msvideo",

    # Audio

    "audio/mpeg",
    "audio/wav",
    "audio/mp3",
]


@router.post(
    "/upload",
    response_model=ImageResponse,
)
def upload_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    if file.content_type not in ALLOWED_TYPES:

        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {file.content_type}",
        )

    metadata = {
        "width": None,
        "height": None,
        "format": None,
    }

    if file.content_type.startswith("image/"):

        metadata = extract_metadata(file)

    filename, file_url = upload_file_to_s3(file)

    ai_data = analyze_file(
        filename=file.filename,
        mime_type=file.content_type,
    )

    image = ImageCreate(
        filename=filename,
        original_filename=file.filename,
        file_path=file_url,
        file_size=0,
        mime_type=file.content_type,
        width=metadata["width"],
        height=metadata["height"],
        image_format=metadata["format"],
        file_category=ai_data["file_category"],
        ai_status=ai_data["ai_status"],
        ai_summary=ai_data["ai_summary"],
        ai_tags=ai_data["ai_tags"],
    )

    return create_image(
        db=db,
        image=image,
        owner_id=current_user.id,
    )


@router.get(
    "",
    response_model=list[ImageResponse],
)
def list_images(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_images_by_owner(
        db,
        current_user.id,
    )


@router.get("/filters")
def get_filters(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    rows = (
        db.query(
            Image.file_category,
            func.count(Image.id),
        )
        .filter(
            Image.owner_id == current_user.id
        )
        .group_by(
            Image.file_category
        )
        .all()
    )

    filters = [
        {
            "name": category or "other",
            "count": count,
        }
        for category, count in rows
    ]

    total = sum(
        item["count"]
        for item in filters
    )

    return {
        "total": total,
        "filters": filters,
    }


@router.get(
    "/{image_id}",
    response_model=ImageResponse,
)
def get_image(
    image_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    image = get_image_by_id(
        db,
        image_id,
    )

    if image is None:

        raise HTTPException(
            status_code=404,
            detail="File not found",
        )

    if image.owner_id != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="Not allowed",
        )

    return image


@router.get("/{image_id}/download")
def download_image(
    image_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    image = get_image_by_id(
        db,
        image_id,
    )

    if image is None:

        raise HTTPException(
            status_code=404,
            detail="File not found",
        )

    if image.owner_id != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="Not allowed",
        )

    download_url = generate_presigned_url(
        image.filename
    )

    return RedirectResponse(
        url=download_url,
    )


@router.delete("/{image_id}")
def remove_image(
    image_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    image = get_image_by_id(
        db,
        image_id,
    )

    if image is None:

        raise HTTPException(
            status_code=404,
            detail="File not found",
        )

    if image.owner_id != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="Not allowed",
        )

    delete_image(
        db,
        image,
    )

    return {
        "message": "File deleted successfully",
    }
