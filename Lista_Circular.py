from xml.dom import minidom

class Pelicula:
    def __init__(self, titulo, director, anio, fecha, hora):
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.fecha = fecha
        self.hora = hora
        self.siguiente = None
        self.anterior = None

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None
        self.anterior = None
        self.peliculas = ListaDoblementeCircularPelicula()  

class ListaDoblementeCircularPelicula:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def vacia(self):
        return self.primero == None
    
    def agregar(self, titulo, director, anio, fecha, hora):
        if self.vacia():
            self.primero = self.ultimo = Pelicula(titulo, director, anio, fecha, hora)
            self.primero.siguiente = self.primero
            self.primero.anterior = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Pelicula(titulo, director, anio, fecha, hora)
            self.ultimo.anterior = aux
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
    
    def agregar_inicio(self, titulo, director, anio, fecha, hora):
        if self.vacia():
            self.primero = self.ultimo = Pelicula(titulo, director, anio, fecha, hora)
            self.primero.siguiente = self.primero
            self.primero.anterior = self.primero
        else:
            aux = Pelicula(titulo, director, anio, fecha, hora)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero

    def eliminar(self, titulo):
        aux = self.primero
        if self.primero.titulo == titulo:
            self.primero = aux.siguiente
            aux.siguiente = None
        else:
            while aux != None:
                if aux.titulo == titulo:
                    aux2.siguiente = aux.siguiente
                    aux.siguiente = None
                    break
                aux2 = aux
                aux = aux.siguiente
                if aux == self.primero:
                    break
    
    def Modificar(self, titulo, director, anio, fecha, hora):
        aux = self.primero
        while aux != None:
            if aux.titulo == titulo:
                aux.director = director
                aux.anio = anio
                aux.fecha = fecha
                aux.hora = hora
                break
            aux = aux.siguiente

   
 


    


class ListaDoblementeCircularCategoria:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def vacia(self):
        return self.primero == None
    
    def AgregarPelicula(self, nombre, titulo, director, anio, fecha, hora):
        aux = self.primero
        while aux != None:
            if aux.nombre == nombre:
                aux.peliculas.agregar(titulo, director, anio, fecha, hora)
                break
            aux = aux.siguiente

    def agregar_final(self, nombre):
        if self.vacia():
            self.primero = self.ultimo = Categoria(nombre)
            self.primero.siguiente = self.primero
            self.primero.anterior = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Categoria(nombre)
            self.ultimo.anterior = aux
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
    
    def agregar_inicio(self, nombre):
        if self.vacia():
            self.primero = self.ultimo = Categoria(nombre)
            self.primero.siguiente = self.primero
            self.primero.anterior = self.primero
        else:
            aux = Categoria(nombre)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
    
    def eliminar(self, nombre):
        aux = self.primero
        if self.primero.nombre == nombre:
            self.primero = self.primero.siguiente
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
        elif self.ultimo.nombre == nombre:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo
        else:
            while aux.siguiente != self.primero:
                if aux.siguiente.nombre == nombre:
                    aux.siguiente = aux.siguiente.siguiente
                    aux.siguiente.anterior = aux
                    break
                aux = aux.siguiente
    
    def Modificar(self, nombre):
        aux = self.primero
        while aux != None:
            if aux.nombre == nombre:
                break
            aux = aux.siguiente
    
    def Mostrar(self):
        aux = self.primero
        while aux != None:
            if aux.siguiente == self.primero:
                print(aux.nombre)
                break
            print(aux.nombre)
            aux = aux.siguiente

    def EliminarCategoria(self, nombre):
        aux = self.primero
        while aux != None:
            if aux.nombre == nombre:
                if aux == self.primero:
                    self.primero = self.primero.siguiente
                    self.primero.anterior = self.ultimo
                    self.ultimo.siguiente = self.primero
                elif aux == self.ultimo:
                    self.ultimo = self.ultimo.anterior
                    self.ultimo.siguiente = self.primero
                    self.primero.anterior = self.ultimo
                else:
                    aux.anterior.siguiente = aux.siguiente
                    aux.siguiente.anterior = aux.anterior
                break
            aux = aux.siguiente

    def ModificarPelicula(self, nombre, titulo, director, anio, fecha, hora):
        aux = self.primero
        while aux != None:
            if aux.nombre == nombre:
                aux.peliculas.Modificar(titulo, director, anio, fecha, hora)
                break
            aux = aux.siguiente
    '''
    <categorias>
        <categoria>
            <nombre>Acción</nombre>
            <peliculas>
                <pelicula>
                    <titulo>Avengers: Endgame</titulo>
                    <director>Joe Russo, Anthony Russo</director>
                    <anio>2019</anio>
                    <fecha>2023-06-05</fecha>
                    <hora>18:30</hora>
                </pelicula>
                <pelicula>
                    <titulo>John Wick</titulo>
                    <director>Chad Stahelski</director>
                    <anio>2014</anio>
                    <fecha>2023-06-06</fecha>
                    <hora>20:00</hora>
                </pelicula>
                <pelicula>
                    <titulo>Misión Imposible: Fallout</titulo>
                    <director>Christopher McQuarrie</director>
                    <anio>2018</anio>
                    <fecha>2023-06-07</fecha>
                    <hora>19:15</hora>
                </pelicula>
            </peliculas>
        </categoria>
        <categoria>
            <nombre>Comedia</nombre>
            <peliculas>
                <pelicula>
                    <titulo>Deadpool</titulo>
                    <director>Tim Miller</director>
                    <anio>2016</anio>
                    <fecha>2023-06-05</fecha>
                    <hora>20:30</hora>
                </pelicula>
                <pelicula>
                    <titulo>Superbad</titulo>
                    <director>Greg Mottola</director>
                    <anio>2007</anio>
                    <fecha>2023-06-06</fecha>
                    <hora>21:00</hora>
                </pelicula>
                <pelicula>
                    <titulo>Bridesmaids</titulo>
                    <director>Paul Feig</director>
                    <anio>2011</anio>
                    <fecha>2023-06-07</fecha>
                    <hora>20:15</hora>
                </pelicula>
            </peliculas>
            </categoria>
    </categorias>
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
    '''
    # Considerar que ambas son listas circulares doblemente enlazadas y necesitan el  break
    # Necesito que coloques el break para ambas listas circulares doblemente enlazadas
    '''
            aux = self.primero
        while aux != None:
            if aux.siguiente == self.primero:
                break
        Un break en el xml como el de la linea anterior
    '''
    def EscribirXmlConBreak(self, numero_de_peliculas):
       document = minidom.Document()
       root = document.createElement('categorias')
       document.appendChild(root)
       aux = self.primero
       contador = 0
       contador2 = 0
       while aux != None:
           Categoria = document.createElement('categoria')
           root.appendChild(Categoria)
           Nombre = document.createElement('nombre')
           Nombre.appendChild(document.createTextNode(aux.nombre))
           Categoria.appendChild(Nombre)
           Peliculas = document.createElement('peliculas')
           Categoria.appendChild(Peliculas)
           aux2 = aux.peliculas.primero 
           print(contador)
           contador += 1
           while aux2 != None:
               Pelicula = document.createElement('pelicula')
               Peliculas.appendChild(Pelicula)
               Titulo = document.createElement('titulo')
               Titulo.appendChild(document.createTextNode(aux2.titulo))
               Pelicula.appendChild(Titulo)
               Director = document.createElement('director')
               Director.appendChild(document.createTextNode(aux2.director))
               Pelicula.appendChild(Director)
               Anio = document.createElement('anio')
               Anio.appendChild(document.createTextNode(aux2.anio))
               Pelicula.appendChild(Anio)
               Fecha = document.createElement('fecha')
               Fecha.appendChild(document.createTextNode(aux2.fecha))
               Pelicula.appendChild(Fecha)
               Hora = document.createElement('hora')
               Hora.appendChild(document.createTextNode(aux2.hora))
               Pelicula.appendChild(Hora)
               aux2 = aux2.siguiente
               print(contador2)
               contador2 += 1
               if contador2 == int(numero_de_peliculas):
                break 
           aux = aux.siguiente
           break   
       xml = document.toprettyxml(indent='\t', newl='\n', encoding='utf-8') 
       xml = xml.decode('utf-8')
       Salida = open('Salida_Categorias.xml', 'w')
       Salida.write(xml)
       Salida.close()   