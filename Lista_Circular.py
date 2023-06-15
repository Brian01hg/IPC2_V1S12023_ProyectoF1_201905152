from Nodo_categoria import Categoria
from Nodo_pelicula import Pelicula
class Lista_pelicula:
    def __init__(self):
        self.primero = None

    def vacia(self):
        return self.primero == None
    
    def agregar_final(self, nombre ,titulo, director, anio, fecha, hora):
        nodo_pelicula = Pelicula(titulo, director, anio, fecha, hora)
        nuevo_nodo = Categoria(nombre, nodo_pelicula)

        if self.primero is None:
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
            self.primero = nuevo_nodo
        else:
            ultimo = self.primero.anterior

            nuevo_nodo.siguiente = self.primero
            nuevo_nodo.anterior = ultimo

            self.primero.anterior = nuevo_nodo
            ultimo.siguiente = nuevo_nodo

    def Mostrar (self):
        if self.vacia():
            print("No hay peliculas registradas")
        else:
            aux = self.primero
            while aux != None:
                print("Nombre: ", aux.nombre)
                print("Titulo: ", aux.peli.titulo)
                print("Director: ", aux.peli.director)
                print("Año: ", aux.peli.anio)
                print("Fecha: ", aux.peli.fecha)
                print("Hora: ", aux.peli.hora)
                aux = aux.siguiente
                if aux == self.primero:
                    break
