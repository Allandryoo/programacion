BBDD = {
    "matrix": {"nombre": "matrix", "duracion": 90, "genero": "ficcion"},
    "star wars": {"nombre": "star wars", "duracion": 140, "genero": "ficcion"},
    "insidious": {"nombre": "insidious", "duracion": 105, "genero": "terror"}
}

opciones = [
    "Salir",
    "Agregar Pelicula",
    "Agregar Genero",
    "Listar Peliculas",
    "Listar Detalles",
    "Informacion Pelicula",
    "Detalle Pelicula",
    "Eliminar Pelicula"
]

generos = [
    "otros",
    "ficcion",
    "terror",
    "comedia",
    "thriller",
    "animacion"
]

salir = False


def agregar_pelicula():

    nombre = input("Indique el nombre de la pelicula\n")

    duracion = int(input("Indique la durcion de la pelicula\n"))

    for pos, gen in enumerate(generos, 1):
        print(f"Para escoger {gen} presione {pos}")

    posicion_generos = int(input("indique el genero de la pelicula\n"))
    genero = generos[posicion_generos-1]

    BBDD.update(
        {nombre: {"nombre": nombre, "duracion": duracion, "genero": genero}}
    )
    print(BBDD)


def agregar_genero():

    genero_agregado = input("indique el genero a agregar\n")
    generos.append(genero_agregado)
    print(generos)


def listar():

    for valor_listado in BBDD.values():
        print(
            f"La pelicula {valor_listado["nombre"]}, tiene una duracion de {valor_listado["duracion"]} y su genero es {valor_listado["genero"]}."
        )


def listado_detallado():

    suma_duracion = 0
    detalles = input("Indique el detalle que desea ver\n")

    if not detalles == "duracion":

        for valor_detallado in BBDD.values():
            print(valor_detallado[detalles])
    else:

        for valor_detallado in BBDD.values():
            print(valor_detallado[detalles])
            suma_duracion += valor_detallado[detalles]

        print(f"La duracion total de las peliculas es {suma_duracion}")

        suma_duracion = 0


def info_pelicula():

    nom_pelicula = input("Indique la pelicula de la que desea informacion\n")

    if nom_pelicula in BBDD.keys():
        print(BBDD[nom_pelicula])
    else:
        print("El nombre de pelicula introducido no existe")


def detalle_pelicula():

    nombre_pelicula = input(
        "Indique el nombre de la pelicula cual desea ver la informacion\n")


while not salir:

    for indice, valor_opciones in enumerate(opciones):
        print(f"Pulsa {indice} para: {valor_opciones}")

    opcion = int(input("Escoge una opcion\n"))

    if opcion == 0:

        print("Has cerrado el programa")
        salir = True

    elif opcion == 1:

        agregar_pelicula()

    elif opcion == 2:

        agregar_genero()

    elif opcion == 3:

        listar()

    elif opcion == 4:

        listado_detallado()

    elif opcion == 5:

        info_pelicula()

    elif opcion == 6:

        detalle_pelicula()
