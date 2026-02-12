import random


class Pokemon:
    def __init__(self, nombre, tipo, ataque, defensa):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque
        self.defensa = defensa
        self.ps = 100
        self.psactual = self.ps
        self.psmax = self.ps

    def get_nombre(self):
        return self.nombre

    def get_tipo(self):
        return self.tipo

    def get_ataque(self):
        return self.ataque

    def get_defensa(self):
        return self.defensa

    def get_ps(self):
        return self.ps

    def set_ps(self, newps):
        self.ps = newps

    def mostrar_info(self):
        return f"Nombre: {self.nombre} | Tipo: {self.tipo} | ATK: {self.ataque} | DEF: {self.defensa} | PS: {self.ps}"


class PokemonPlanta(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa):
        super().__init__(nombre, tipo, ataque, defensa)
        self.tipo = "Planta"

        def ataque_especial(self):
            self.ataque *= 2


class PokemonAgua(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa):
        super().__init__(nombre, tipo, ataque, defensa)
        self.tipo = "Agua"

        def ataque_especial(self):
            self.ataque *= 2


class PokemonFuego(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa):
        super().__init__(nombre, tipo, ataque, defensa)
        self.tipo = "Fuego"

        def ataque_especial(self):
            self.ataque *= 2


class PokemonVolador(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa):
        super().__init__(nombre, tipo, ataque, defensa)
        self.tipo = "Volador"

        def ataque_especial(self):
            self.ataque *= 2


class Mapa:
    def __init__(self, lado):
        self.lado = lado
        self.mapa = []

    def generar_mapa(self):
        for y in range(1, self.lado+1):
            for x in range(1, self.lado+1):
                self.mapa.append([None, (x, y)])

    def mostrar_mapa(self):
        linea = ""
        for i in self.mapa:
            if i[0] == None:
                linea += str(f"[Ninguno ,{i[1]}]")
            else:
                linea += str(f"[{i[0].get_nombre()},{i[1]}]")
            if i[1][0] == self.lado:
                print(linea)
                linea = ""

    def pokemon_mapa(self, pokemon, x, y):
        for i in self.mapa:
            if i[1][0] == x and i[1][1] == y:
                if i[0] == None:
                    i[0] = pokemon

    def añadir_pokemons(self):
        for i in self.mapa:
            if i[0] == None and random.randint(0, 2) == random.randint(0, 2):
                i[0] = almacen[random.randint(0, len(almacen)-1)]


class Personaje:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover_izquierda(self):
        self.x -= 1

    def mover_derecha(self):
        self.x += 1

    def mover_arriba(self):
        self.y += 1

    def mover_abajo(self):
        self.y -= 1


class Jugador(Personaje):
    def __init__(self, x, y, nombre):
        super().__init__(x, y)
        self.nombre = nombre
        self.inventario = []

    def capturar_pokemon(self, pokemon):
        vida_max = pokemon.get_ps()
        if pokemon.get_ps() > (vida_max*0.75):
            probabilidad_captura = 30
        elif pokemon.get_ps() <= (vida_max*0.75):
            probabilidad_captura = 50
        elif pokemon.get_ps() <= (vida_max*0.50):
            probabilidad_captura = 70
        elif pokemon.get_ps() <= (vida_max*0.25):
            probabilidad_captura = 100

        exito_captura = random.randint(0, 100)

        if probabilidad_captura >= exito_captura:
            print(f"{pokemon.get_nombre()} ha sido capturado")
        else:
            print(f"{pokemon.get_nombre()} ha escapado")

    def llamar_pokemon(self):
        numero_random = random.randint(0, len(almacen)-1)

        self.inventario.append(almacen[numero_random])
        almacen.pop(numero_random)


def procesar_linea(linea):
    campos = []
    actual = ""

    for c in linea:
        if c == ",":
            campos.append(actual)
            actual = ""
        else:
            actual += c

    campos.append(actual)

    nombre = campos[0]
    tipo = campos[1].lower()
    ataque = int(campos[2])
    defensa = int(campos[3])

    match tipo:
        case "planta":
            return PokemonPlanta(nombre, tipo, ataque, defensa)
        case "agua":
            return PokemonAgua(nombre, tipo, ataque, defensa)
        case "fuego":
            return PokemonFuego(nombre, tipo, ataque, defensa)
        case "volador":
            return PokemonVolador(nombre, tipo, ataque, defensa)


def escoger_pokemon():
    print("Escoge un pokemon\n")
    for indice, valor in enumerate(p1.inventario):
        print(f"{indice}: {valor.mostrar_info()}")

    num_pokemon = int(
        input("Indica el numero del pokemon para seleccionarlo\n"))
    return num_pokemon


def combate_pokemon(mipokemon, pokemonsalvaje):
    miataque = mipokemon.get_ataque()
    mipsactual = mipokemon.get_ps()
    mipsmax = mipokemon.get_ps()
    midef = mipokemon.get_defensa()
    enemyataque = pokemonsalvaje.get_ataque()
    enemypsmax = pokemonsalvaje.get_ps()
    enemypsactual = pokemonsalvaje.get_ps()
    enemydef = pokemonsalvaje.get_defensa()

    if mipokemon.tipo == "planta" and pokemonsalvaje.tipo == "agua":
        miataque = mipokemon.ataque_especial()
        enemyataque = pokemonsalvaje.get_ataque()/2
    elif mipokemon.tipo == "fuego" and pokemonsalvaje.tipo == "planta":
        miataque = mipokemon.ataque_especial()
        enemyataque = pokemonsalvaje.get_ataque()/2
    elif mipokemon.tipo == "agua" and pokemonsalvaje.tipo == "fuego":
        miataque = mipokemon.ataque_especial()
        enemyataque = pokemonsalvaje.get_ataque()/2

    while enemypsactual >= 0 or mipsactual >= 0:

        print(f"{mipokemon.get_nombre()} salud:{mipsactual} | | {pokemonsalvaje.get_nombre()} salud:{enemypsactual}")

        luchar = input("Que quieres hacer :(a)atacar | (c)capturar")

        match luchar.lower():

            case "a":
                if miataque <= enemyataque:
                    print("miss")
                else:
                    print("Daño")


almacen = []

with open(r"UD4\Pokemon\pokemons.txt") as lista_pokemons:
    for contenedor_texto in lista_pokemons:
        contenedor_texto = contenedor_texto.strip()
        pokemon = procesar_linea(contenedor_texto)
        almacen.append(pokemon)

planta = 0
fuego = 0
agua = 0
volador = 0
for i in almacen:

    match i.tipo.lower():

        case "planta":
            print(f"{i.nombre} es un pokemon de tipo {i.tipo}, fuerte contra agua")
            planta += 1
        case "fuego":
            print(f"{i.nombre} es un pokemon de tipo {i.tipo}, fuerte contra planta")
            fuego += 1
        case "agua":
            print(f"{i.nombre} es un pokemon de tipo {i.tipo}, fuerte contra fuego")
            agua += 1
        case "volador":
            print(f"{i.nombre} es un pokemon de tipo {i.tipo}, fuerte contra roca")
            volador += 1

    if len(almacen) - (planta + fuego + agua + volador) == 0:
        print(f"Pokemons tipo Planta: {planta}")
        print(f"Pokemons tipo Fuego: {fuego}")
        print(f"Pokemons tipo Agua: {agua}")
        print(f"Pokemons tipo Volador: {volador}")
        print(f"Total de Pokemons añadidos: {planta + fuego + agua + volador}")

mapa_pokemon = Mapa(5)
mapa_pokemon.generar_mapa()
mapa_pokemon.mostrar_mapa()
p1 = Jugador(1, 1, "alan")

p1.llamar_pokemon()
p1.llamar_pokemon()
for j in p1.inventario:
    print(j.get_nombre())
for i in almacen:
    print(i.mostrar_info())

mapa_pokemon.pokemon_mapa(almacen[random.randint(0, len(almacen)-1)], 4, 4)
mapa_pokemon.pokemon_mapa(almacen[random.randint(0, len(almacen)-1)], 2, 2)
mapa_pokemon.añadir_pokemons()
mapa_pokemon.mostrar_mapa()
print("hola")
mapa_pokemon.mostrar_mapa()
salir = True
print(p1.x, p1.y)
while salir:
    move = input("donde quieres ir?")

    match move:

        case "w":
            if p1.y < mapa_pokemon.lado:
                p1.mover_arriba()
        case "d":
            if p1.x < mapa_pokemon.lado:
                p1.mover_derecha()
        case "s":
            if p1.y > 1:
                p1.mover_abajo()
        case "a":
            if p1.x > 1:
                p1.mover_izquierda()

    print(f"posicion acutal: ({p1.x},{p1.y})")
    mapa_pokemon.mostrar_mapa()
    for i in mapa_pokemon.mapa:
        if i[1][0] == p1.x and i[1][1] == p1.y:
            if i[0] != None:
                print(
                    f"Te has encontrado a {i[0].get_nombre()} de tipo {i[0].get_tipo()}")
                select_pokemon = (p1.inventario[escoger_pokemon()])
                print(f"Te escojo a ti {select_pokemon.get_nombre()}")
                combate_pokemon(select_pokemon, i[0])

            else:
                print("no hay pokemon")
