keys = [
    "price",
    "object number",
    "object type en",
    "object type de",
    "object type ru",
    "floor",
    "closed area",
    "total area",
    "rooms",
    "bedrooms",
    "terrace",
    "balcony",
    "pool",
    "completion"
]

keys_de = [
    "preis",
    "objektnummer",
    "objekttyp",
    "etage",
    "nutzfläche",
    "gesamtfläche",
    "räume",
    "schlafzimmer",
    "terasse",
    "balkon",
    "pool",
    "fertigstellung"
]

keys_ru = [
    "цена",
    "номер объекта",
    "тип объекта",
    "этаж",
    "площадь",
    "общая площадь",
    "команты",
    "спальни",
    "терасса",
    "балкон",
    "бассейн",
    "срок сдачи"
]

values = [''] * len(keys)

editor_keys = [
    "номер",
    "ссылка",
    "удалить"
]

keys_en = [i.replace(' ', '') for i in keys]
en_attr_key = {'price': 'price', 'objectnumber': 'object number', 'objecttypeen': 'object type', 'floor': 'floor',
               'closedarea': 'closed area', 'totalarea': 'total area', 'rooms': 'rooms', 'bedrooms': 'bedrooms',
               'terrace': 'terrace', 'balcony': 'balcony', 'pool': 'pool', 'completion': 'completion'}
de_attr_key = {'price': 'preis', 'objectnumber': 'objektnummer', 'objecttypede': 'objekttyp', 'floor': 'etage',
               'closedarea': 'nutzfläche', 'totalarea': 'gesamtfläche', 'rooms': 'räume', 'bedrooms': 'schlafzimmer',
               'terrace': 'terasse', 'balcony': 'balkon', 'pool': 'pool', 'completion': 'fertigstellung'}
ru_attr_key = {'price': 'цена', 'objectnumber': 'номер объекта', 'objecttyperu': 'тип объекта', 'floor': 'этаж',
               'closedarea': 'площадь', 'totalarea': 'общая площадь', 'rooms': 'команты', 'bedrooms': 'спальни',
               'terrace': 'терасса', 'balcony': 'балкон', 'pool': 'бассейн', 'completion': 'срок сдачи'}
