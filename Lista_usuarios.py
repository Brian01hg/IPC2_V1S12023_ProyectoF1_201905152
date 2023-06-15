from Nodo_usuarios import Usuario
from xml.dom import minidom
class Lista_usuarios:

    def __init__(self):
        self.primero = None
    
    def vacia(self):
        return self.primero == None

    def agregar_final(self, rol, nombre, apellido, correo, contraseña, telefono):
        if self.vacia():
            self.primero = Usuario(rol, nombre, apellido, correo, contraseña, telefono)
        else:
            aux = self.primero
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = Usuario(rol, nombre, apellido, correo, contraseña, telefono)

    def agregar_inicio(self, rol, nombre, apellido, correo, contraseña, telefono):
        if self.vacia():
            self.primero = Usuario(rol, nombre, apellido, correo, contraseña, telefono)
        else:
            aux = Usuario(rol, nombre, apellido, correo, contraseña, telefono)
            aux.siguiente = self.primero
            self.primero = aux

    def eliminarPorCorreo(self, correo):
        if self.vacia():
            print("No hay usuarios registrados")
        else:
            aux = self.primero
            while aux != None:
                if aux.correo == correo:
                    if aux == self.primero:
                        self.primero = aux.siguiente
                        aux.siguiente = None
                        break
                    else:
                        aux2.siguiente = aux.siguiente
                        aux.siguiente = None
                        break
                aux2 = aux
                aux = aux.siguiente
                if aux == self.primero:
                    break
    
    def ModificarPorCorreo(self, correo, nombre, apellido, contraseña, telefono):
        if self.vacia():
            print("No hay usuarios registrados")
        else:
            aux = self.primero
            while aux != None:
                if aux.correo == correo:
                    aux.nombre = nombre
                    aux.apellido = apellido
                    aux.contraseña = contraseña
                    aux.telefono = telefono
                    break
                aux = aux.siguiente
    
    def mostrar(self):
        aux = self.primero
        while aux != None:
            print("Rol: ", aux.rol)
            print("Nombre: ", aux.nombre)
            print("Apellido: ", aux.apellido)
            print("Correo: ", aux.correo)
            print("Contraseña: ", aux.contraseña)
            print("Telefono: ", aux.telefono)
            print("")
            aux = aux.siguiente
    
    def buscar(self, correo):
        aux = self.primero
        while aux != None:
            if aux.correo == correo:
                return aux
            else:
                aux = aux.siguiente
        return None
    

    
    def Inicio_Session(self, correo, contraseña):
        aux = self.primero
        while aux != None:
            if aux.correo == correo and aux.contraseña == contraseña:
                return True
            else:
                aux = aux.siguiente
        return False

    def EscribirArchivo(self):
        document = minidom.Document()
        root = document.createElement('usuarios')
        document.appendChild(root)
        aux = self.primero
        while aux != None:
            Usuario = document.createElement('usuario')
            root.appendChild(Usuario)
            Nombre = document.createElement('nombre')
            Nombre.appendChild(document.createTextNode(aux.nombre))
            Usuario.appendChild(Nombre)
            Apellido = document.createElement('apellido')
            Apellido.appendChild(document.createTextNode(aux.apellido))
            Usuario.appendChild(Apellido)
            Correo = document.createElement('correo')
            Correo.appendChild(document.createTextNode(aux.correo))
            Usuario.appendChild(Correo)
            Telefono = document.createElement('telefono')
            Telefono.appendChild(document.createTextNode(aux.telefono))
            Usuario.appendChild(Telefono)
            Rol = document.createElement('rol')
            Rol.appendChild(document.createTextNode(aux.rol))
            Usuario.appendChild(Rol)
            Password = document.createElement('password')
            Password.appendChild(document.createTextNode(aux.contraseña))  
            Usuario.appendChild(Password)
            aux = aux.siguiente
        xml = document.toprettyxml(indent='\t', newl='\n', encoding='utf-8') 
        xml = xml.decode('utf-8')
        Salida = open('Salida_Usuarios.xml', 'w')
        Salida.write(xml)
        Salida.close()

'''
lista = Lista_usuarios()
lista.agregar_final("Administrador", "Juan", "Perez", "juan@gmail.com" , "1234", "12345678")
lista.mostrar()
print("")
lista.agregar_final("Cliente", "Pedro", "Perez", "Pedro@gmai.com" , "1234", "12345678")
lista.mostrar()
print("")
lista.EscribirArchivo()
'''

