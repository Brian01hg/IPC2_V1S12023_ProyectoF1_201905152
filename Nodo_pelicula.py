# Lista Circular Doblemente enlazada
class Pelicula:
    def __init__(self, titulo, director, anio, fecha, hora):
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.fecha = fecha
        self.hora = hora
        self.siguiente = None
        self.anterior = None