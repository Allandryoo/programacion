altos =5
anchos =5



def crear_mapa(ancho, alto, objeto_x=None, objeto_y=None, simbolo=" 1 "): 
    mapa = [[" · " for _ in range(ancho)] for _ in range(alto)] 
    if objeto_x is not None and objeto_y is not None: 
        mapa[objeto_y][objeto_x] = simbolo 
        for fila in mapa: print("".join(fila)) 
        

crear_mapa(altos, anchos, 3, 4)
