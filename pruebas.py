contador =0
base =2
binario=input("binario\n")
PosAct=len(binario)-1
    

for i in range(0,len(binario)):
    contador += (int(binario[i])*base)**PosAct
    PosAct-=1

print(contador)