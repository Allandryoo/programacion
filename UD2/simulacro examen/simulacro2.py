import random

salir = False

recetario = {}

ingredientes = ["Coger tomate y ",
                "Coger pollo y ",
                "Coger huevo y ",
                "Coger lechuga y ",
                "Coger queso y ",
                "Coger zanahoria y "]

acciones = ["cortar con ",
            "mezclar con ",
            "especiar con ",
            "batir con ",
            "congelar con "]

utensilios = ["cuchillo.",
              "batidiora.",
              "mortero.",
              "cuchara.",
              "tenedor."]

menu_opciones = ["Salir",
                 "Agregar ingrediente",
                 "Agregar accion",
                 "Agregar utensilio",
                 "Mostrar ingredientes",
                 "Mostrar acciones",
                 "Mostrar utensilios",
                 "Crear instruccion",
                 "Crear receta",
                 "Crear libro",
                 "Mostrar recetario"]


def numero_random(lista_random):

    numero_aleatorio = random.randint(1, len(lista_random)-1)
    return numero_aleatorio


def agregar_ingrediente(ingrediente_agregado):

    ingredientes.append("coger "+ingrediente_agregado + " y ")


def agregar_accion(accion_agregada):

    acciones.append(accion_agregada + " con ")


def agregar_utensilio(utensilio_agregado):

    utensilios.append(utensilio_agregado)


def mostrar_ingredientes():

    print(ingredientes)


def mostrar_acciones():

    print(acciones)


def mostrar_utensilios():

    print(utensilios)


def crear_instruccion():

    instruccion = (ingredientes[numero_random(ingredientes)] + acciones[numero_random(
        acciones)] + utensilios[numero_random(utensilios)])

    return instruccion


def crear_receta(numero_pasos):
    lista_recetas = []
    for i in range(1, numero_pasos+1):
        lista_recetas.append(crear_instruccion())
    return lista_recetas


def crear_libro(nombre_libro, numero_recetas):

    for i in range(1, numero_recetas+1):
        numero = int(input(f"Indica el numero de pasos para la receta {i}"))
        recetario[nombre_libro] = {f"receta{i}": crear_receta(numero)}


while not salir:

    print("\n-----------------------------------------------")
    print("              Menu de opciones")
    print("-----------------------------------------------")
    for posicion_lista, opcion_lista in enumerate(menu_opciones):
        print(f"Presiona {posicion_lista} para: {opcion_lista}.")
    print("-----------------------------------------------")
    opcion = int(input("Escoe una opcion:\n"))

    if opcion == 0:

        print("Hoy no comes")
        salir = True

    elif opcion == 1:

        ingrediente_agregado = input(
            "Indique el ingrediente que desear añadir.\n")
        agregar_ingrediente(ingrediente_agregado)
        print(ingredientes)

    elif opcion == 2:

        accion_agregada = input(
            "Indique la accion que desear añadir.\n")
        agregar_accion(accion_agregada)
        print(acciones)

    elif opcion == 3:

        utensilio_agregado = input(
            "indique el utensilio que desea añadir.\n")
        agregar_utensilio(utensilio_agregado)
        print(utensilios)

    elif opcion == 4:

        mostrar_ingredientes()

    elif opcion == 5:

        mostrar_acciones()

    elif opcion == 6:

        mostrar_utensilios()

    elif opcion == 7:

        instruccion_creada = crear_instruccion()
        print(instruccion_creada)

    elif opcion == 8:

        numero_pasos = int(input("Indique el numero de pasos:\n"))
        print(crear_receta(numero_pasos))

    elif opcion == 9:

        nombre_libro = input("Indique el nombre del libro:\n")
        numero_recetas = int(input("Indique el numero de recetas:\n"))

        crear_libro(nombre_libro, numero_recetas)

    elif opcion == 10:

        print(recetario)
