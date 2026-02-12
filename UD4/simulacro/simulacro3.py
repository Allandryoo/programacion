class Curso:
    def __init__(self, codigo, titulo, horas, precio):
        self.codigo = codigo
        self.titulo = titulo
        self.horas = horas
        self.precio = precio

    def mostrar_info(self):
        return f"Codigo:{self.codigo} | Titulo:{self.titulo} |Horas:{self.horas} | Precio:{self.precio}"
    
    def precio_final(self):
        preciofinal = self.horas * self.precio
        return preciofinal
    
class CursoOnline(Curso):
    def __init__(self, codigo, titulo, horas, precio, plataforma):
        super().__init__(codigo, titulo, horas, precio)
        self.plataforma = plataforma

    def mostrar_info(self):
        return f"Codigo:{self.codigo} | Titulo:{self.titulo} | Horas:{self.horas} | Precio:{self.precio} | Plataforma:{self.plataforma}"
    
    def precio_final(self):
        preciofinal = self.horas * self.precio
        return preciofinal
    
class CursoPresencial(Curso):
    def __init__(self, codigo, titulo, horas, precio, aula):
        super().__init__(codigo, titulo, horas, precio)
        self.aula = aula

    def mostrar_info(self):
        return f"Codigo:{self.codigo} | Titulo:{self.titulo} | Horas:{self.horas} | Precio:{self.precio} | Aula:{self.aula}"
    
    def precio_final(self):
        if self.horas > 40:
            preciofinal = self.horas * (self.precio *1.15)
            return preciofinal 
        else:
            preciofinal = self.horas * self.precio
            return preciofinal
        

c1 = CursoPresencial(1,"DAW",51,12,"4A")
c2 = CursoPresencial(2,"DAM",38,12,"4A")
c3 = CursoOnline(3,"ASIX", 45, 11, "Netflix")
listacursos=[c1,c2,c3]
for i in listacursos:
    cursos = {c1.codigo:c1.titulo}

print(cursos)