import random

numrandom=random.randint(1,10)

print(numrandom)
numero=int(input("Intenta adivinar el numero entre 1 y 10\n"))

while numrandom!=numero:
    numero=int(input("Intentalo de nuevo\n"))

print("Acertaste")