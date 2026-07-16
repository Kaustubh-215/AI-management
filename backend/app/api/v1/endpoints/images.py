from fastapi import (
    APIRouter,
    Depends,
    File,
    HTTPException,
    UploadFile,
)

from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.crud.image import (
    create_image,
    delete_image,
    get_image_by_id,
    get_images_by_owner,
)
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
    "image/gif",

    # PDF / Documents

    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",

    # Excel

    "application/vnd.ms-excel",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

    # CSV / TSV

    "text/csv",
    "text/tab-separated-values",
    "application/csv",

    # Text

    "text/plain",

    # ZIP / Archive

    "application/zip",
    "application/x-zip-compressed",

    # Video

    "video/mp4",
    "video/mpeg",
    "video/quicktime",

    # Audio

    "audio/mpeg",
    "audio/mp3",
    "audio/wav",
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

    # Extract metadata only for images

    if file.content_type.startswith("image/"):

        metadata = extract_metadata(file)

    # AI analysis

    ai_data = analyze_file(
        filename=file.filename,
        mime_type=file.content_type,
    )

    # Upload to S3

    filename, file_url = upload_file_to_s3(file)

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

    if image is None or image.owner_id != current_user.id:

        raise HTTPException(
            status_code=404,
            detail="File not found",
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

    if image is None or image.owner_id != current_user.id:

        raise HTTPException(
            status_code=404,
            detail="File not found",
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

    if image is None or image.owner_id != current_user.id:

        raise HTTPException(
            status_code=404,
            detail="File not found",
        )

    delete_image(
        db,
        image,
    )

    return {
        "message": "File deleted successfully",
    }
