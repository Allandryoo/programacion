import random

class Pokemon:
    def __init__(self, nombre, tipo, ataque, defensa, ps):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque
        self.defensa = defensa
        self.ps = 100

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
    def __init__(self, nombre, tipo, ataque, defensa, ps):
        super().__init__(nombre, tipo, ataque, defensa, ps)
        self.tipo = "Planta"

        def ataque_especial(self):
            self.ataque *= 2

class PokemonAgua(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa, ps):
        super().__init__(nombre, tipo, ataque, defensa, ps)
        self.tipo = "Agua"

        def ataque_especial(self):
            self.ataque *= 2

class PokemonFuego(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa, ps):
        super().__init__(nombre, tipo, ataque, defensa, ps)
        self.tipo = "Fuego"

        def ataque_especial(self):
            self.ataque *= 2

class PokemonVolador(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa, ps):
        super().__init__(nombre, tipo, ataque, defensa, ps)
        self.tipo = "Volador"

        def ataque_especial(self):
            self.ataque *= 2

class Mapa:
    def __init__(self, lado):
        self.lado = lado
        self.mapa = []
        self.listavacia=[]

    def generar_mapa(self): 
        for y in range(1,self.lado+1): 
            for x in range(1,self.lado+1): 
                self.mapa.append([None, (x,y)])

    def mostrar_mapa(self):
        linea=""
        for i in self.mapa:
            if i[0] == None:
                linea += str(f"[Ninguno ,{i[1]}]")
            else:
                linea += str(f"[{i[0].get_nombre()},{i[1]}]")
            if i[1][0] == self.lado:
                print(linea)
                linea=""
    
    def pokemon_mapa(self, pokemon, x, y):

        for i in self.mapa:
            if i[1][0] == x and i[1][1] == y:
                if i[0] == None:
                    i[0] = pokemon
        
    def añadir_pokemons(self):
        for i in self.mapa:
                if i[0] == None:
                    i[0] = almacen[random.randint(0,len(almacen)-1)]

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

    def capturar_pokemon(self, pokemon):
        pass

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
            return PokemonPlanta(nombre, tipo, ataque, defensa, 100)
        case "agua":
            return PokemonAgua(nombre, tipo, ataque, defensa, 100)
        case "fuego":
            return PokemonFuego(nombre, tipo, ataque, defensa, 100)
        case "volador":
            return PokemonVolador(nombre, tipo, ataque, defensa, 100)

almacen = []

with open(r"C:\Users\ALLANDRYOSANTOSDACON\Documents\programacion_sjo\UD4\Pokemon\pokemons.txt") as lista_pokemons: 
    for linea in lista_pokemons: 
        linea = linea.strip() 
        pokemon = procesar_linea(linea) 
        almacen.append(pokemon)

planta=0
fuego=0
agua=0
volador=0
for i in almacen:

    match i.tipo.lower():

        case "planta":
            print(f"{i.nombre} es un pokemon de tipo {i.tipo}, fuerte contra agua")
            planta +=1
        case "fuego":
            print(f"{i.nombre} es un pokemon de tipo {i.tipo}, fuerte contra planta")
            fuego +=1
        case "agua":
            print(f"{i.nombre} es un pokemon de tipo {i.tipo}, fuerte contra fuego")
            agua +=1
        case "volador":
            print(f"{i.nombre} es un pokemon de tipo {i.tipo}, fuerte contra roca")
            volador +=1

    if len(almacen) - (planta + fuego + agua + volador) == 0:
        print(f"Pokemons tipo Planta: {planta}")
        print(f"Pokemons tipo Fuego: {fuego}")
        print(f"Pokemons tipo Agua: {agua}")
        print(f"Pokemons tipo Volador: {volador}")
        print(f"Total de Pokemons añadidos: {planta + fuego + agua + volador}")

mapa_pokemon = Mapa(5)
mapa_pokemon.generar_mapa()
mapa_pokemon.pokemon_mapa(almacen[random.randint(0,len(almacen)-1)], 4, 4)
mapa_pokemon.pokemon_mapa(almacen[random.randint(0,len(almacen)-1)], 2, 2)
mapa_pokemon.añadir_pokemons()
mapa_pokemon.mostrar_mapa()
#mapa_pokemon.mapa_detallado(almacen)

