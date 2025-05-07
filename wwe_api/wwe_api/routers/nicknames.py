from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from wwe_api.db import get_db
from wwe_api.models import Nickname

from wwe_api.schemas import NicknameSchema, NicknamesResponse


nicknames_router = APIRouter(prefix="/nicknames")

@nicknames_router.get("/")
def get_nicknames(
    db: Annotated[Session, Depends(get_db)]
) -> NicknamesResponse:
    response = []
    query = db.query(Nickname)
    results = query.all()
    for nickname in results:
        nickname_data = NicknameSchema(
            name=nickname.name
        )
        response.append(nickname_data)

    return NicknamesResponse(nicknames=response)
