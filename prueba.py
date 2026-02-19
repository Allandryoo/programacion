class p:
    def __init__(self, nom):
        self.nom = nom
        self.lsita=[]

    def añadir(self, aña):
        self.lsita.append(aña)

class da:
    def __init__(self, nom, tip):
        self.nom = nom
        self.tip = tip
p1=p("a")

a=da("das","dsa")
b=da("afs","fas")

lista=["hola","adios","ay"]
p1.añadir(a)
p1.añadir(b)

p1.lsita.remove(a)
for i in p1.lsita:
    print(i.nom)