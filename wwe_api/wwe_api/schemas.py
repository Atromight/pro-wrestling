from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from wwe_api.const import WeightClass

class WrestlerOutput(BaseModel):
    name: str
    birth_date: datetime
    world_titles: int
    weight_class: WeightClass
    active: bool
    debut: int
    # age: int

    class Config:
        from_attributes = True

class WrestlersResponse(BaseModel):
    wrestlers: List[WrestlerOutput]