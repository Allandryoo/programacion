class Animal:
    def __init__(self, nombre, especie, edad, peso, sonido):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso
        self.sonido = sonido

    def get_nombre(self):
        return self.nombre
    
    def get_especie(self):
        return self.especie
    
    def get_edad(self):
        return self.edad
    
    def get_peso(self):
        return self.peso

    def get_sonido(self):
        return self.sonido

    def set_nombre(self, newnom):
        self.nombre = newnom

    def set_especie(self, newesp):
        self.especie = newesp

    def set_edad(self, neweda):
        if neweda >0:
            self.edad = neweda
        else:
            print("No se puede asignar un valor negativo")
    
    def set_peso(self, newpes):
        if newpes >0:
            self.edad = newpes
        else:
            print("No se puede asignar un valor negativo")

    def set_sonido(self, newson):
        self.sonido = newson

    def hacer_sonido(self):
        return f"{self.nombre} hace {self.sonido}"
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Especie: {self.especie} - Edad: {self.edad}años - Peso{self.peso}kg"
    

class Clinica:
    def __init__(self):
        self.lista_animales = []

    def ingresar_animal(self, animal):
        self.lista_animales.append(animal)

    def mostrar_pacientes(self):
        for i in self.lista_animales:
            print(f"{i.mostrar_info()}, {i.hacer_sonido()}")
    
    def buscar_por_nombre(self, nombre):
        for i in self.lista_animales:
            if i.nombre == nombre:
                i.mostrar_info()
        else:
            print("El animal no existe en la base de datos")


        
p1 = Animal("firulais", "perro", 7, 12, "GUAU")
g1 = Animal("michi", "gato", 4, 5, "MIAU")

clinica = Clinica()

clinica.ingresar_animal(p1)
clinica.ingresar_animal(g1)