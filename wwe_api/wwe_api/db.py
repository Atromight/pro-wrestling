from wwe_api.const import WeightClass

def get_wrestlers_db():
    wrestlers_db = [
        {"id": 1, "name": "Hulk Hogan", "birth_date": "1953-08-11", "world_titles": 12, "nickname": "Immortal", "weight_class": WeightClass.HEAVYWEIGHT},
        {"id": 2, "name": "Steve Austin", "birth_date": "1964-12-18", "world_titles": 6, "nickname": "Rattlesnake", "weight_class": WeightClass.MIDDLEWEIGHT},
        {"id": 3, "name": "Ric Flair", "birth_date": "1949-02-25", "world_titles": 16, "nickname": "Nature Boy", "weight_class": WeightClass.MIDDLEWEIGHT},
        {"id": 4, "name": "The Rock", "birth_date": "1972-05-02", "world_titles": 10, "nickname": "People's Champ", "weight_class": WeightClass.HEAVYWEIGHT},
        {"id": 5, "name": "John Cena", "birth_date": "1977-04-23", "world_titles": 17, "nickname": "Doctor of Thuganomics", "weight_class": WeightClass.HEAVYWEIGHT},
        {"id": 6, "name": "CM Punk", "birth_date": "1978-10-26", "world_titles": 5, "nickname": "Best in the World", "weight_class": WeightClass.MIDDLEWEIGHT},
        {"id": 7, "name": "Roman Reigns", "birth_date": "1985-05-25", "world_titles": 6, "nickname": "Tribal Chief", "weight_class": WeightClass.HEAVYWEIGHT},
        {"id": 8, "name": "Brock Lesnar", "birth_date": "1977-07-12", "world_titles": 10, "nickname": "Beast Incarnate", "weight_class": WeightClass.HEAVYWEIGHT},
        {"id": 9, "name": "Rey Mysterio", "birth_date": "1974-12-11", "world_titles": 3, "nickname": "Ultimate Underdog", "weight_class": WeightClass.LIGHTWEIGHT}
    ]
    return wrestlers_db