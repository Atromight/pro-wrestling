from typing import Optional

from fastapi import FastAPI

app = FastAPI()
db = [
    {"id": 1, "name": "Hulk Hogan", "birth_date": "1953-08-11", "reigns": 12, "nickname": "Immortal", "weight_category": "Heavy"},
    {"id": 2, "name": "Steve Austin", "birth_date": "1964-12-18", "reigns": 6, "nickname": "Rattlesnake", "weight_category": "Midddle"},
    {"id": 3, "name": "Ric Flair", "birth_date": "1949-02-25", "reigns": 16, "nickname": "Nature Boy", "weight_category": "Middle"},
    {"id": 4, "name": "The Rock", "birth_date": "1972-05-02", "reigns": 10, "nickname": "People's Champ", "weight_category": "Heavy"},
    {"id": 5, "name": "John Cena", "birth_date": "1977-04-23", "reigns": 17, "nickname": "Doctor of Thuganomics", "weight_category": "Heavy"},
    {"id": 6, "name": "CM Punk", "birth_date": "1978-10-26", "reigns": 5, "nickname": "Best in the World", "weight_category": "Middle"},
    {"id": 7, "name": "Roman Reigns", "birth_date": "1985-05-25", "reigns": 6, "nickname": "Tribal Chief", "weight_category": "Heavy"},
    {"id": 8, "name": "Brock Lesnar", "birth_date": "1977-07-12", "reigns": 10, "nickname": "Beast Incarnate", "weight_category": "Heavy"}
]

@app.get("/")
async def welcome():
    return{"message": "THEN, NOW, FOREVER, TOGETHER!"}

@app.get("/wrestlers")
def get_wrestlers(reigns: Optional[int]):
    return db