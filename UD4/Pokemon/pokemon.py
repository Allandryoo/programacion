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

def procesar_linea(linea):
    campos = []
    actual = ""

    for c in linea:
        if c == ",":
            campos.append(actual)
            actual = ""
        else:
            actual += c

    campos.append(actual)  # último campo

    nombre = campos[0]
    tipo = campos[1].lower()
    ataque = int(campos[2])
    defensa = int(campos[3])

    # -----------------------------
    # Crear el objeto Pokémon correcto
    # -----------------------------
    if tipo == "planta":
        return PokemonPlanta(nombre, tipo, ataque, defensa, 100)
    elif tipo == "agua":
        return PokemonAgua(nombre, tipo, ataque, defensa, 100)
    elif tipo == "fuego":
        return PokemonFuego(nombre, tipo, ataque, defensa, 100)
    elif tipo == "volador":
        return PokemonVolador(nombre, tipo, ataque, defensa, 100)
    else:
        return Pokemon(nombre, tipo, ataque, defensa, 100)

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

    if i.tipo.lower() == "planta":
        planta =planta +1
    elif i.tipo.lower() == "fuego":
        fuego +=1
    elif i.tipo.lower() == "agua":
        agua +=1
    elif i.tipo.lower() == "volador":
        volador +=1

    if len(almacen) - (planta + fuego + agua + volador) == 0:
        print(f"Pokemons tipo Planta: {planta}")
        print(f"Pokemons tipo Fuego: {fuego}")
        print(f"Pokemons tipo Agua: {agua}")
        print(f"Pokemons tipo Volador: {volador}")
        print(f"Total de Pokemons añadidos: {planta + fuego + agua + volador}")