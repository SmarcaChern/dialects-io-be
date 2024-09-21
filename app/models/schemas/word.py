from pydantic import BaseModel

from app.models.schemas.utils import CustomDateTime


class Character(BaseModel):
    """字"""


class Word(BaseModel):
    """词"""


class Source(BaseModel):
    """出处"""
