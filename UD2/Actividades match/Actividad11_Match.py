def primo(n):
            for i in range(2,n):
                if n%i == 0:
                    print("No es primo")
                    return True
        
            print("Es primo")
            return False

num=int(input("Introduce un numero: "))

print("1 Para hacer su factoial\n2 Para comprobar si es primo")
opcion=int(input("Escoge una opcion: "))
match opcion:
    case 1:
        for i in range(num-1,1,-1):
            num*=i
        print(num)
    case 2:
        primo(num)
        