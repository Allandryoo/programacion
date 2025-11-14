BBDD = {
    "matrix": {"nombre": "matrix", "duracion": 90, "genero": "ficcion"},
    "star wars": {"nombre": "star wars", "duracion": 140, "genero": "ficcion"},
    "insidious": {"nombre": "insidious", "duracion": 105, "genero": "terror"}
}

info = input("detalles")

for key, valor in BBDD.items():

    if info in key:
        print(key, valor)
    else:
        print("El nombre de pelicula introducido no existe")
