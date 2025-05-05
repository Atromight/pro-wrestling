from datetime import datetime
import pandas as pd
from sqlalchemy.orm import Session

from wwe_api.const import CSV_PATHS
from wwe_api.db import SessionLocal
from wwe_api.models import Wrestler


def load_wrestler_data(db: Session):
    path = CSV_PATHS["wrestler"]
    df = pd.read_csv(path)
    for _, row in df.iterrows():
        birth_date = datetime.strptime(row["birth_date"], "%Y-%m-%d").date()
        wrestler = Wrestler(
            id=row["id"],
            name=row["name"],
            birth_date=birth_date,
            world_titles=int(row["world_titles"]),
            weight_class=row["weight_class"],
            active=row["active"],
            debut=int(row["debut"]),
        )
        db.add(wrestler)


def load_all_csv_data():
    db = SessionLocal()
    try:
        if db.query(Wrestler).count() == 0:
            load_wrestler_data(db) # Only load the CSV if the table is empty.

        db.commit()
    finally:
        db.close()