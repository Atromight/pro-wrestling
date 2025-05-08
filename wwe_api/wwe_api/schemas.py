from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from wwe_api.const import WeightClass


class NicknameSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True


class NicknamesResponse(BaseModel):
    nicknames: List[NicknameSchema]

class WrestlerSchema(BaseModel):
    name: str
    birth_date: datetime
    world_titles: int
    weight_class: WeightClass
    active: bool
    debut: int
    age: int
    nicknames: Optional[List[NicknameSchema]] = []

    class Config:
        from_attributes = True


class WrestlerResponse(BaseModel):
    wrestler: WrestlerSchema


class WrestlersResponse(BaseModel):
    wrestlers: List[WrestlerSchema]
