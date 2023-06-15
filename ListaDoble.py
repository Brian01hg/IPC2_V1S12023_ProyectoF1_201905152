from xml.dom import minidom
class Nodo_Salas:
    def __init__(self, numero, asientos):
        self.numero = numero
        self.asientos = asientos
        self.anterior = None
        self.siguiente = None


class ListaDobleSalas:
    def __init__(self):
        self.primero = None

    def is_empty(self):
        return self.primero is None

    def append(self, numero, asientos):
        nodo_nuevo = Nodo_Salas(numero, asientos)
        if self.is_empty():
            self.primero = nodo_nuevo
        else:
            tmp = self.primero
            while tmp.siguiente:
                tmp = tmp.siguiente
            tmp.siguiente = nodo_nuevo
            nodo_nuevo.anterior = tmp

    def prepend(self, numero, asientos):
        nodo_nuevo = Nodo_Salas(numero, asientos)
        if self.is_empty():
            self.primero = nodo_nuevo
        else:
            nodo_nuevo.siguiente = self.primero
            self.primero.anterior = nodo_nuevo
            self.primero = nodo_nuevo

    def delete(self, numero):
        tmp = self.primero
        while tmp:
            if tmp.numero == numero:
                if tmp.anterior:
                    tmp.anterior.siguiente = tmp.siguiente
                else:
                    self.primero = tmp.siguiente
                if tmp.siguiente:
                    tmp.siguiente.anterior = tmp.anterior
                return True
            tmp = tmp.siguiente
        return False

    def show(self):
        tmp = self.primero
        while tmp:
            print(tmp.numero, tmp.asientos)
            tmp = tmp.siguiente


class Nodo_Cines:
    def __init__(self, nombre):
        self.nombre = nombre
        self.anterior = None
        self.siguiente = None
        self.salas = ListaDobleSalas()  


class ListaDobleCines:
    def __init__(self):
        self.primero = None

    def is_empty(self):
        return self.primero is None

    def append(self, nombre):
        nodo_nuevo = Nodo_Cines(nombre)
        if self.is_empty():
            self.primero = nodo_nuevo
        else:
            tmp = self.primero
            while tmp.siguiente:
                tmp = tmp.siguiente
            tmp.siguiente = nodo_nuevo
            nodo_nuevo.anterior = tmp

    def prepend(self, nombre):
        nodo_nuevo = Nodo_Cines(nombre)
        if self.is_empty():
            self.primero = nodo_nuevo
        else:
            nodo_nuevo.siguiente = self.primero
            self.primero.anterior = nodo_nuevo
            self.primero = nodo_nuevo
    
    def AgregarSala(self, nombre, numero, asientos):
        tmp = self.primero
        while tmp:
            if tmp.nombre == nombre:
                tmp.salas.append(numero, asientos)
                return True
            tmp = tmp.siguiente
        return False

    def delete(self, nombre):
        tmp = self.primero
        while tmp:
            if tmp.nombre == nombre:
                if tmp.anterior:
                    tmp.anterior.siguiente = tmp.siguiente
                else:
                    self.primero = tmp.siguiente
                if tmp.siguiente:
                    tmp.siguiente.anterior = tmp.anterior
                return True
            tmp = tmp.siguiente
        return False

    def show(self):
        tmp = self.primero
        while tmp:
            print(tmp.nombre)
            tmp.salas.show()  
            tmp = tmp.siguiente

    '''
    <cines>
        <cine>
            <nombre>Cine ABC</nombre>
            <salas>
                <sala>
                    <numero>#USACIPC2_202212333_1</numero>
                    <asientos>100</asientos>
                </sala>
                <sala>
                    <numero>#USACIPC2_202212333_2</numero>
                    <asientos>80</asientos>
                </sala>
                <sala>
                    <numero>#USACIPC2_202212333_3</numero>
                    <asientos>120</asientos>
                </sala>
            </salas>
            </cine>
    </cines>
    '''
    def EscribirArchivo(self):
        document = minidom.Document()
        root = document.createElement('cines')
        document.appendChild(root)
        aux = self.primero
        while aux != None:
            Cine = document.createElement('cine')
            root.appendChild(Cine)
            Nombre = document.createElement('nombre')
            Nombre.appendChild(document.createTextNode(aux.nombre))
            Cine.appendChild(Nombre)
            Salas = document.createElement('salas')
            Cine.appendChild(Salas)
            aux2 = aux.salas.primero
            while aux2 != None:
                Sala = document.createElement('sala')
                Salas.appendChild(Sala)
                Numero = document.createElement('numero')
                Numero.appendChild(document.createTextNode(aux2.numero))
                Sala.appendChild(Numero)
                Asientos = document.createElement('asientos')
                Asientos.appendChild(document.createTextNode(aux2.asientos))
                Sala.appendChild(Asientos)
                aux2 = aux2.siguiente
            aux = aux.siguiente
        xml = document.toprettyxml(indent='\t', newl='\n', encoding='utf-8') 
        xml = xml.decode('utf-8')
        Salida = open('Salida_Cines.xml', 'w')
        Salida.write(xml)
        Salida.close()
