import random

class Persona:
    def __init__(self, nombre, resistencia, altura, posx, posy):
        self.nombre = nombre
        self.resistencia = resistencia
        self.altura = altura
        self.posx = posx 
        self.posy = posy

    def mostrar_posicion(self):
        print(f"Posicion actual:({self.posx}, {self.posy})")
        print(f"Resistencia:{self.resistencia}")
        if self.posx == 0 and self.posy == 0:
            self.resistencia = self.resistencia + 10
            print("Has recuperado la resistencia")
            print(self.resistencia)

    def arriba(self):
        if self.posy < 5:
            self.posy = self.posy + 1
            self.resistencia = self.resistencia - 1
        else:
            print("Te vas a caer del mapa")
        self.mostrar_posicion()

    def abajo(self):
        if self.posy > 0:
            self.posy = self.posy - 1
            self.resistencia = self.resistencia - 1
        else:
            print("Te vas a caer del mapa")
        self.mostrar_posicion()

    def izquierda(self):
        if self.posx > 0:
            self.posx = self.posx - 1
            self.resistencia = self.resistencia - 1
        else:
            print("Te vas a caer del mapa")
        self.mostrar_posicion()

    def derecha(self):
        if self.posx < 5:
            self.posx = self.posx + 1
            self.resistencia = self.resistencia - 1
        else:
            print("Te vas a caer del mapa")
        self.mostrar_posicion()

    def teletransporte(self):
        x = int(input("Posicion X: "))
        y = int(input("Posicion Y: "))
        if x >= 0 and x <= 5 and y >= 0 and y <= 5:
            self.posx = x
            self.posy = y
            self.resistencia = self.resistencia - 5
        else:
            print("No puedo moverme")
        self.mostrar_posicion()

aleatoriox = random.randint(0,5)
aleatorioy = random.randint(0,5)

persona1 = Persona("Alan", 10, 1.85, 0, 0)
print(f"Posicion actual:({persona1.posx}, {persona1.posy})")

persona2 = Persona("Ionut", 10, 1.70, aleatoriox, aleatorioy)
print(persona2.posx,persona2.posy)

while persona1.resistencia > 0:

    if persona1.posx == persona2.posx and persona1.posy == persona2.posy:
        print(f"Muy bien atrapaste a {persona2.nombre}")

    opcion = input("A donde quieres ir?\n")

    match opcion:

        case "w":
            persona1.arriba()

        case "s":
            persona1.abajo()

        case "a":
            persona1.izquierda()

        case "d":
            persona1.derecha()

        case "goku":
            persona1.teletransporte()

        case _:
            print("Has salido del juego")
            break
print("Te has quedado sin resistencia")