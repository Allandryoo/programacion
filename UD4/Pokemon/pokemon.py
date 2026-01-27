almacen=[]

def almacen_pokemon():
    pass        
with open(r"C:\Users\ALLANDRYOSANTOSDACON\Documents\programacion_sjo\UD4\Pokemon\pokemons.txt") as lista_pokemons:
    for linea in lista_pokemons:
            almacen.append(linea.strip())
print(almacen)

planta = 0
volador = 0
fuego = 0
agua = 0
        
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