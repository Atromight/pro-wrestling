from datetime import datetime
from typing import Annotated, Optional

from fastapi import APIRouter, Query

from wwe_api.const import BIRTH_DATE_FMT, WeightClass
from wwe_api.db import get_wrestlers_db
from wwe_api.models import Wrestler, WrestlersResponse


wrestlers_router = APIRouter(prefix="/wrestlers")

@wrestlers_router.get("/")
def get_wrestlers(
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
    wrestlers_db = get_wrestlers_db()
    response = WrestlersResponse(wrestlers=[])
    for wrestler in wrestlers_db:
        if weight_class and wre:
            response.wrestlers.append(Wrestler(**wrestler))
    if weight_class:       
        response = [Wrestler(**wrestler) for wrestler in wrestlers_db if wrestler["weight_class"] == weight_class]

    # if birth_date_gte:
    #     for wrestler in response:
    #         if datetime.strptime(wrestler["birth_date"], BIRTH_DATE_FMT) < birth_date_gte:
    #             response.append(wrestler)

    return response
