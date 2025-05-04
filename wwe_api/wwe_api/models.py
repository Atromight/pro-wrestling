from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from wwe_api.const import WeightClass

class Wrestler(BaseModel):
    name: str
    birth_date: datetime
    world_titles: int
    nickname: Optional[str]
    weight_class: WeightClass

class WrestlersResponse(BaseModel):
    wrestlers: List[Wrestler]