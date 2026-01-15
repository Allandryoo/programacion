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
            return f"Has ingresado {cantidaddeposito}, Tu saldo ahora es de: {self.saldo}€"

    def retirar(self, cantidadretirada):
        if cantidadretirada <= self.saldo:
            self.saldo = self.saldo - cantidadretirada
            return f"Has retirado {cantidadretirada}, Tu saldo ahora es de: {self.saldo}€"
        elif cantidadretirada < 0:
            print("No puede retirar una cantidad negativa")
        else:
            print("No dispone de tanta cantidad")
    
    def transferencia(self, cantidatransferir, cuentadestino):
        if cantidatransferir <= self.saldo and cantidatransferir > 0:
            cuentadestino.saldo = cuentadestino.saldo + cantidatransferir
            self.saldo = self.saldo - cantidatransferir
            return f"Has enviado {cantidatransferir}€ a {cuentadestino.nombre} con IBAN:{cuentadestino.iban}"
        else:
            print("Cantidad erronea")

class CuentaRecompensa(CuentaBancaria):
    def __init__(self, nombre, saldo, iban):
        super().__init__(nombre, saldo, iban)

    def obtener_saldo(self):
        return f"saldo actual: {self.saldo}€"

    def transferencia(self, cantidatransferir, cuentadestino):
        if cantidatransferir <= self.saldo and cantidatransferir > 0:
            cuentadestino.saldo = cuentadestino.saldo + cantidatransferir
            self.saldo = self.saldo - cantidatransferir
        else:
            print("Cantidad erronea")

    def depositar(self, cantidaddeposito):
        if cantidaddeposito < 0:
            print("No puede ingresar una cantidad negativa")
        else:
            self.saldo = self.saldo + (cantidaddeposito * 1.05)

    def retirar(self, cantidadretirada):
        if cantidadretirada <= self.saldo:
            self.saldo = self.saldo - cantidadretirada
        elif cantidadretirada < 0:
            print("No puede retirar una cantidad negativa")
        else:
            print("No dispone de tanta cantidad")

class CuentaAhorros(CuentaBancaria):
    def __init__(self, nombre, saldo, iban):
        super().__init__(nombre, saldo, iban)

    def obtener_saldo(self):
        return f"saldo actual: {self.saldo}€"

    def transferencia(self, cantidatransferir, cuentadestino):
        if cantidatransferir <= self.saldo and cantidatransferir > 0:
            cuentadestino.saldo = cuentadestino.saldo + cantidatransferir
            self.saldo = self.saldo - cantidatransferir
        else:
            print("Cantidad erronea")

    def depositar(self, cantidaddeposito):
        if cantidaddeposito < 0:
            print("No puede ingresar una cantidad negativa")
        else:
            self.saldo = self.saldo + cantidaddeposito

    def retirar(self, cantidadretirada):
        if (cantidadretirada + 5) <= self.saldo:
            self.saldo = self.saldo - cantidadretirada - 5
        elif cantidadretirada < 0:
            print("No puede retirar una cantidad negativa")
        else:
            print("No dispone de la cantidad suficiente")

cuenta1 = CuentaBancaria("alan", 3000, 12345)
cuenta2 = CuentaBancaria("boy", 100, 23456)

cuentainteres = CuentaRecompensa("Alan", 1000, 34567)

cuentahorros = CuentaAhorros("Alan", 1000, 45678)

print(f"{cuenta1.nombre}, saldo {cuenta1.saldo}€ con IBAN: {cuenta1.iban}")
print(f"{cuenta2.nombre}, saldo {cuenta2.saldo}€ con IBAN: {cuenta2.iban}")

cuenta1.depositar(500)
print(cuenta1.saldo)
cuenta1.retirar(1000)
print(cuenta1.saldo)
print(cuenta2.saldo)
cuenta1.transferencia(1000, cuenta2)
print(cuenta2.saldo)

print(cuentainteres.saldo)
cuentainteres.depositar(100)
print(cuentainteres.saldo)

print(cuentahorros.saldo)
cuentahorros.retirar(100)
print(cuentahorros.saldo)
