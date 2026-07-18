from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ImageBase(BaseModel):
    filename: str
    original_filename: str
    file_path: str
    file_size: int
    mime_type: str

    width: Optional[int] = None
    height: Optional[int] = None
    image_format: Optional[str] = None

    file_category: Optional[str] = None

    ai_status: Optional[str] = "pending"
    ai_summary: Optional[str] = None
    ai_tags: Optional[str] = None


class ImageCreate(ImageBase):
    pass


class ImageResponse(ImageBase):
    id: int
    owner_id: int
    uploaded_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
