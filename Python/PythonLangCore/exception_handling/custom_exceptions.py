


class DataQualityError(Exception):
    pass


class MissingColumnError(DataQualityError):
    pass

def validate(row, required):
    missing = [c for c in required if c not in row]
    if missing:
        raise MissingColumnError(f"missing columns: {missing}")
    return True



rows = [
    {"orderNumber": 1, "productCode": "S18_1749", "qty": 30},
    {"orderNumber": 2, "qty": 10},
]


for row in rows:

    try:
        validate(row,["orderNumber", "productCode", "qty"])
        print(row, "-> OK")
    except MissingColumnError as e:
        print(e)
