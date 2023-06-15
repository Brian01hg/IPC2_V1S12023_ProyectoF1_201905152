class Sala:
    def __init__(self, categoria, nombre, numero, asientos):
        self.categoria = categoria
        self.nombre = nombre
        self.numero = numero
        self.asientos = asientos
        self.siguiente = None
        self.anterior = None