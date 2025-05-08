from datetime import date, datetime
from typing import Annotated, Optional

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Path,
    Query,
    status
)
from sqlalchemy import func, select
from sqlalchemy.orm import joinedload, Session

from wwe_api.const import BIRTH_DATE_FMT, WeightClass
from wwe_api.db import get_db
from wwe_api.models import Wrestler
from wwe_api.schemas import (
    NicknameSchema,
    WrestlerSchema,
    WrestlerResponse,
    WrestlersResponse
)


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
    ] = None,
    limit: Annotated[
        Optional[int],
        Query(description="Number of rows to fetch")
    ] = 20,
    skip: Annotated[
        Optional[int],
        Query(description="Number of rows to skip")
    ] = 0,
    include_nicknames: Annotated[
        bool,
        Query(description="Whether to include the nicknames of each wrestler")
    ] = False,
    include_moves: Annotated[
        Optional[bool],
        Query(description="Whether to include the move names of each wrestler")
    ] = False,
) -> WrestlersResponse:

    response = []

    today = date.today()

    # Calculating age as (current year - birth year) for simplicity
    age_expr = func.strftime('%Y', func.date('now')) - func.strftime('%Y', Wrestler.birth_date)

    query = db.query(Wrestler)

    if include_nicknames:
        query = query.options(joinedload(Wrestler.nicknames))

    if weight_class:
        query = query.filter(Wrestler.weight_class == weight_class)

    if birth_date_gte:
        query = query.filter(Wrestler.birth_date >= birth_date_gte)

    if birth_date_lte:
        query = query.filter(Wrestler.birth_date <= birth_date_gte)

    if limit:
        query = query.limit(limit)

    if skip:
        query = query.offset(skip)

    query = query.add_columns(age_expr.label("age"))

    results = query.all()

    for wrestler, age in results:
        wrestler_data = WrestlerSchema(
            name=wrestler.name,
            birth_date=wrestler.birth_date,
            world_titles=wrestler.world_titles,
            weight_class=wrestler.weight_class,
            active=wrestler.active,
            debut=wrestler.debut,
            age=int(age),
        )
        if include_nicknames:
            wrestler_data.nicknames = [
                NicknameSchema.from_orm(nickname) for nickname in wrestler.nicknames
            ]

        response.append(
            wrestler_data
        )

    return WrestlersResponse(wrestlers=response)

@wrestlers_router.get("/{wrestler_id}")
def get_wrestler(
    db: Annotated[Session, Depends(get_db)],
    wrestler_id: Annotated[
        int,
        Path(description="ID for the wrestler to fetch", ge=1)
    ]
) -> WrestlerResponse:
    try:
        wrestler = db.query(Wrestler).get(wrestler_id)
        if not wrestler:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Wrestler not found"
            )

        # Add this in separate function?
        today = date.today()
        age = today.year - wrestler.birth_date.year

        # Add the population of Schemas in separate functions?
        wrestler_data = WrestlerSchema(
            name=wrestler.name,
            birth_date=wrestler.birth_date,
            world_titles=wrestler.world_titles,
            weight_class=wrestler.weight_class,
            active=wrestler.active,
            debut=wrestler.debut,
            age=int(age),
        )

        return WrestlerResponse(
            wrestler=wrestler_data
        )

    except HTTPException as e:
        # If the exception is raised already, fastapi will catch it
        raise e

    except Exception as e:
        # logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred. Please try again later."
        )
