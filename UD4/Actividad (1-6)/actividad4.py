class coche:

    def __init__(self, marca, modelo, potencia, color, matriculacion, siguiente_revision):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.color = color
        self.matriculacion = matriculacion
        self.siguiente_revision = siguiente_revision

    def mostrar(self):
        print (f"Marca: {self.marca}, Modelo: {self.modelo}, Potencia: {self.potencia}, Color: {self.color}, Año matriculacion: {self.matriculacion}, Revision: {self.siguiente_revision}.") 

    def acelerar(Self):
        self.potencia = self.potencia +10