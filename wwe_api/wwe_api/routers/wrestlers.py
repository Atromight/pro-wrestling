from datetime import datetime
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from wwe_api.const import BIRTH_DATE_FMT, WeightClass
from wwe_api.db import get_db
from wwe_api.models import Wrestler
from wwe_api.schemas import WrestlerOutput, WrestlersResponse


wrestlers_router = APIRouter(prefix="/wrestlers")

@wrestlers_router.get("/")
def get_wrestlers(
    db: Annotated[Session, Depends(get_db)],
    weight_class: Annotated[
        Optional[WeightClass],
        Query(enum=[wc for wc in WeightClass], description="Weight Category of Wrestler")
    ] = None,
    birth_date_gte: Annotated[
        Optional[datetime],
        Query(description="Minimum birth date for wrestler")
    ] = None,
    birth_date_lte: Annotated[
        Optional[datetime],
        Query(description="Maximum birth date for wrestler")
    ] = None
) -> WrestlersResponse:
    response = []
    wrestlers = db.query(Wrestler).all()
    for row in wrestlers:
        wrestler_dict = WrestlerOutput.from_orm(row).dict()
        response.append(wrestler_dict)

    return WrestlersResponse(wrestlers=response)
        
    # if weight_class:       
    #     response = [Wrestler(**wrestler) for wrestler in wrestlers_db if wrestler["weight_class"] == weight_class]

    # if birth_date_gte:
    #     for wrestler in response:
    #         if datetime.strptime(wrestler["birth_date"], BIRTH_DATE_FMT) < birth_date_gte:
    #             response.append(wrestler)

