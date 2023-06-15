from Nodo_salas import Sala 
from xml.dom import minidom
class ListaSalas:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero is None

    def agregar_final(self, nombre, numero, asientos):
        nueva_sala = Sala(nombre, numero, asientos)
        if self.vacia():
            self.primero = nueva_sala
            self.ultimo = nueva_sala
        else:
            nueva_sala.anterior = self.ultimo
            self.ultimo.siguiente = nueva_sala
            self.ultimo = nueva_sala

    def mostrar(self):
        aux = self.primero
        while aux is not None:
            print("Nombre: ", aux.nombre)
            print("Número: ", aux.numero)
            print("Asientos: ", aux.asientos)
            print("")
            aux = aux.siguiente

    def agregar_sala(lista_salas):
     nombre = input("Ingrese el nombre de la sala: ")
     numero = input("Ingrese el número de la sala: ")
     asientos = input("Ingrese la cantidad de asientos: ")
     lista_salas.agregar_final(nombre, numero, asientos)
     print("Sala agregada correctamente.")        

    def escribir_archivo(self, nombre_archivo):
        document = minidom.Document()
        root = document.createElement('salas')
        document.appendChild(root)
        aux = self.primero
        while aux is not None:
            sala_element = document.createElement('sala')
            root.appendChild(sala_element)
            
            nombre_element = document.createElement('nombre')
            nombre_element.appendChild(document.createTextNode(aux.nombre))
            sala_element.appendChild(nombre_element)
            
            numero_element = document.createElement('numero')
            numero_element.appendChild(document.createTextNode(aux.numero))
            sala_element.appendChild(numero_element)
            
            asientos_element = document.createElement('asientos')
            asientos_element.appendChild(document.createTextNode(str(aux.asientos)))
            sala_element.appendChild(asientos_element)
            
            aux = aux.siguiente

        xml = document.toprettyxml(indent='\t', newl='\n', encoding='utf-8')
        with open(nombre_archivo, 'w') as file:
            file.write(xml)
        
        

