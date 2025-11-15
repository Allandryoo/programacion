BBDD = {
    "matrix": {"nombre": "matrix", "duracion": 90, "genero": "ficcion"},
    "star wars": {"nombre": "star wars", "duracion": 140, "genero": "ficcion"},
    "insidious": {"nombre": "insidious", "duracion": 105, "genero": "terror"}
}

info = input("nombre")


for genero in (BBDD.values()):
    print(f"Indique que detalle desea ver {genero.keys()}")

det = int(input(""))
genpos = BBDD.values()[det]

for key, values in BBDD.items():

    if info in key:

        print(f"{key} tiene una duracion de {values[genpos]}")
