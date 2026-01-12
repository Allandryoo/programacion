class CuentaBancaria:
    def __init__(self, nombre, saldo, iban):
        self.nombre = nombre
        self.saldo = saldo
        self.iban = iban

    def obtener_saldo(self):
        return f"saldo actual: {self.saldo}€"
    
    def depositar(self, cantidaddeposito):
        if cantidaddeposito < 0:
            print("No puede ingresar una cantidad negativa")
        else:
            self.saldo = self.saldo + cantidaddeposito

    def retirar(self, cantidadretirada):
        if cantidadretirada <= self.saldo:
            self.saldo = self.saldo - cantidadretirada
        elif cantidadretirada < 0:
            print("No puede retirar una cantidad negativa")
        else:
            print("No dispone de tanta cantidad")
    
    def transferencia(self, cantidatransferir, cuentadestino):
        if cantidatransferir <= self.saldo and cantidatransferir > 0:
            cuentadestino.saldo = cuentadestino.saldo + cantidatransferir
            self.saldo = self.saldo - cantidatransferir
        else:
            print("Cantidad erronea")

class CuentaRecompensa(CuentaBancaria):
    def __init__(self, nombre, saldo, iban):
        super().__init__(nombre, saldo, iban)

    def transferencia(self, cantidatransferir, cuentadestino):
        if cantidatransferir <= self.saldo and cantidatransferir > 0:
            cuentadestino.saldo = cuentadestino.saldo + cantidatransferir
            self.saldo = self.saldo - cantidatransferir - 5
        else:
            print("Cantidad erronea")

class CuentaAhorros(CuentaBancaria):
    def __init__(self, nombre, saldo, iban):
        super().__init__(nombre, saldo, iban)

    def transferencia(self, cantidatransferir, cuentadestino):
        if cantidatransferir <= self.saldo and cantidatransferir > 0:
            cuentadestino.saldo = cuentadestino.saldo + cantidatransferir
            self.saldo = self.saldo - cantidatransferir
        else:
            print("Cantidad erronea")

cuenta1 = CuentaBancaria("alan", 3000, 12345)
cuenta2 = CuentaBancaria("boy", 100, 23456)

print(f"{cuenta1.nombre}, saldo {cuenta1.saldo}€ con IBAN: {cuenta1.iban}")
print(f"{cuenta2.nombre}, saldo {cuenta2.saldo}€ con IBAN: {cuenta2.iban}")

cuenta1.depositar(500)
print(cuenta1.saldo)
cuenta1.retirar(1000)
print(cuenta1.saldo)
print(cuenta2.saldo)
cuenta1.transferencia(1000, cuenta2)
print(cuenta2.saldo)