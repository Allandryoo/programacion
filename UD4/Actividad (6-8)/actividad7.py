class libros:
    
    def __init__(self, titulo, autor, genero, paginas):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.paginas = paginas

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor

    def get_genero(self):
        return self.genero