from typing import Optional, List

from pydantic import BaseModel, validator


class Config(BaseModel):
    token: str = ''
    author_id: int = 0
    timer: int = 0
    checkpoint_timer: int = 0
    interval: int = 0
    multiple: int = 0
    maximum: int = 0
    webhook: Optional[str] = ''
    sheet_url: Optional[str] = ''
    channels_id: List[int] = []

    @validator("interval", "checkpoint_timer", "interval", pre=True, always=True)
    def _min_to_sec(cls, value: int):
        return value * 60
