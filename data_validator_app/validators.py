import re

EMAIL_REGEX = re.compile(r"^[^@]+@[^@]+\.[^@]+$")

def validate_row(row, row_number):
    errors = []

    # a) número de columnas
    if len(row) != 5:
        errors.append({
            "row": row_number,
            "column": "ALL",
            "message": "El archivo debe tener exactamente 5 columnas"
        })
        return errors

    # b) Columna 1: enteros entre 3 y 10 caracteres
    if not row[0].isdigit() or not (3 <= len(row[0]) <= 10):
        errors.append({
            "row": row_number,
            "column": 1,
            "message": "Debe ser número entero entre 3 y 10 caracteres"
        })

    # c) Columna 2: email
    if not EMAIL_REGEX.match(row[1]):
        errors.append({
            "row": row_number,
            "column": 2,
            "message": "Correo electrónico inválido"
        })

    # d) Columna 3: CC o TI
    if row[2] not in ("CC", "TI"):
        errors.append({
            "row": row_number,
            "column": 3,
            "message": "Solo se permiten valores CC o TI"
        })

    # e) Columna 4: número entre 500000 y 1500000
    try:
        value = int(row[3])
        if not (500000 <= value <= 1500000):
            raise ValueError
    except ValueError:
        errors.append({
            "row": row_number,
            "column": 4,
            "message": "Debe estar entre 500000 y 1500000"
        })

    # f) Columna 5: cualquier valor → NO se valida

    return errors
