from enum import StrEnum


BIRTH_DATE_FMT = "%Y-%m-%d"

class WeightClass(StrEnum):
    HEAVYWEIGHT = "Heavyweight"
    MIDDLEWEIGHT = "Middleweight"
    LIGHTWEIGHT = "Lightweight"