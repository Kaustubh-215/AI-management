from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ImageBase(BaseModel):
    filename: str
    original_filename: str
    file_path: str
    file_size: int
    mime_type: str

    width: int | None = None
    height: int | None = None
    image_format: str | None = None

    file_category: str | None = None

    ai_status: str | None = None
    ai_summary: str | None = None
    ai_tags: str | None = None


class ImageCreate(ImageBase):
    pass


class ImageResponse(ImageBase):
    id: int
    owner_id: int
    uploaded_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
