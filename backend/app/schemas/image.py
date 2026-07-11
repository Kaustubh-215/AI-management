from datetime import datetime

from pydantic import BaseModel


class ImageCreate(BaseModel):
    filename: str
    original_filename: str
    file_path: str
    file_size: int
    mime_type: str

    width: int | None = None
    height: int | None = None
    image_format: str | None = None


class ImageResponse(BaseModel):
    id: int
    filename: str
    original_filename: str
    file_size: int
    mime_type: str

    width: int | None = None
    height: int | None = None
    image_format: str | None = None

    uploaded_at: datetime

    class Config:
        from_attributes = True
