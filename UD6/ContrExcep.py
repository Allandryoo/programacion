class cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def ingresar_dinero(self, cantidad):
        self.saldo = self.saldo + cantidad

    def retirar_dinero(self, cantidad):
        self.saldo = self.saldo - cantidad

def ingresar(cliente):
    print(f"Saldo: {cliente.saldo}")
    cantidad = int(input("Indica la cantidad a ingresar\n"))
    cliente.ingresar_dinero(cantidad)

c1 = cliente("A", 1000)

while True:
    try:
        ingresar(c1)
    except ValueError:
        print("Valor erroneo")
