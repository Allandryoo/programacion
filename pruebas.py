lista = [10, 20, 30, 40]

# Opción 1: pop() - elimina y devuelve el valor
elemento = lista.pop(1)  # Elimina posición 1 (valor 20)
print(elemento)  # 20
print(lista)     # [10, 30, 40]

# Opción 2: del - solo elimina
del lista[2]     # Elimina posición 2
print(lista)     # [10, 30]

# Opción 3: remove() - elimina por valor, no por posición
lista.remove(30) # Busca y elimina el valor 30
print(lista)     # [10]
