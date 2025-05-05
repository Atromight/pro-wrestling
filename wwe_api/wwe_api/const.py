from enum import StrEnum


BIRTH_DATE_FMT = "%Y-%m-%d"

CSV_PATHS = {
    "wrestler": "wwe_api/data/tWrestler.csv"
}

class WeightClass(StrEnum):
    SUPERHEAVYWEIGHT = "superheavyweight"
    HEAVYWEIGHT = "heavyweight"
    MIDDLEWEIGHT = "middleweight"
    LIGHTWEIGHT = "lightweight"