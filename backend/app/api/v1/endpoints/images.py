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
    "image/jpeg",
    "image/png",
    "image/webp",
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
            detail="Invalid image type",
        )

    metadata = extract_metadata(file)

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
            detail="Image not found",
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
            detail="Image not found",
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
            detail="Image not found",
        )

    delete_image(
        db,
        image,
    )

    return {
        "message": "Image deleted successfully"
    }
