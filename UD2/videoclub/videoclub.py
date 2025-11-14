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
suma_duracion = 0


def agregar_pelicula(nombre, duracion, genero):

    BBDD.update(
        {nombre: {"nombre": nombre, "duracion": duracion, "genero": genero}}
    )


def agregar_genero(genero_agregado):

    generos.append(genero_agregado)


def info_pelicula(nom_pelicula):

    for llave, valores in BBDD.items():
        if nom_pelicula in llave:
            print(llave, valores)
        else:
            print("El nombre de pelicula introducido no existe")


while not salir:

    for indice, valor in enumerate(opciones):
        print(f"Pulsa {indice} para: {valor}")

    opcion = int(input("Escoge una opcion\n"))

    if opcion == 0:

        print("Has cerrado el programa")
        salir = True

    elif opcion == 1:

        nombre_pelicula = input("Indique el nombre de la pelicula\n")

        duracion_pelicula = int(input("Indique la durcion de la pelicula\n"))

        for indice, gen in enumerate(generos, 1):
            print(f"Para escoger {gen} presione {indice}")

        posicion_generos = int(input("indique el genero de la pelicula\n"))
        genero_pelicula = generos[posicion_generos-1]

        agregar_pelicula(nombre_pelicula, duracion_pelicula, genero_pelicula)

    elif opcion == 2:
        genero_sumado = input("indique el genero a agregar\n").lower

        agregar_genero(genero_sumado)
        print(generos)

    elif opcion == 3:

        for key, valor in BBDD.items():
            print(
                f"La pelicula {valor["nombre"]}, tiene una duracion de {valor["duracion"]} y su genero es {valor["genero"]}.")

    elif opcion == 4:

        detalles = input("Indique el detalle que desea ver\n")

        if not detalles == "duracion":

            for valor in BBDD.values():
                print(valor[detalles])
        else:

            for valor in BBDD.values():
                print(valor[detalles])
                suma_duracion += valor[detalles]

            print(f"La duracion total de las peliculas es {suma_duracion}")

            suma_duracion = 0

    elif opcion == 5:

        info_peli = input("Indique la pelicula de la que desea informacion\n")

        info_pelicula(info_peli)
