from sqlalchemy.orm import Session

from app.models.image import Image
from app.schemas.image import ImageCreate
from app.services.s3 import delete_file_from_s3


def create_image(
    db: Session,
    image: ImageCreate,
    owner_id: int,
):
    db_image = Image(
        filename=image.filename,
        original_filename=image.original_filename,
        file_path=image.file_path,
        file_size=image.file_size,
        mime_type=image.mime_type,

        owner_id=owner_id,

        width=image.width,
        height=image.height,
        image_format=image.image_format,

        file_category=image.file_category,

        ai_status=image.ai_status,
        ai_summary=image.ai_summary,
        ai_tags=image.ai_tags,
    )

    db.add(db_image)

    db.commit()

    db.refresh(db_image)

    return db_image


def get_images_by_owner(
    db: Session,
    owner_id: int,
):
    return (
        db.query(Image)
        .filter(Image.owner_id == owner_id)
        .order_by(Image.uploaded_at.desc())
        .all()
    )


def get_image_by_id(
    db: Session,
    image_id: int,
):
    return (
        db.query(Image)
        .filter(Image.id == image_id)
        .first()
    )


def delete_image(
    db: Session,
    image: Image,
):
    delete_file_from_s3(
        image.filename
    )

    db.delete(image)

    db.commit()

