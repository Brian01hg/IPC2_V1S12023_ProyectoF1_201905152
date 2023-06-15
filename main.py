from xml.dom import minidom
from Lista_usuarios import Lista_usuarios
from Lista_Circular import Lista_pelicula
from Lista_Doble import ListaSalas
def cargar_salas_desde_xml(lista_salas, archivo_xml):
    try:
        doc = minidom.parse(archivo_xml)
        salas = doc.getElementsByTagName("sala")

        for sala in salas:
            nombre = sala.getElementsByTagName("nombre")[0].firstChild.data
            numero = sala.getElementsByTagName("numero")[0].firstChild.data
            asientos = int(sala.getElementsByTagName("asientos")[0].firstChild.data)

            lista_salas.agregar_inicio(nombre, numero, asientos)

    except FileNotFoundError:
        print(f"El archivo {archivo_xml} no se encontró.")
    except Exception as e:
        print("Ocurrió un error al cargar el archivo XML:", str(e))

cargar_salas_desde_xml(ListaSalas, "salas_cine.xml")

lista = Lista_usuarios()
licas = Lista_pelicula()
listasalas = ListaSalas()

lista.agregar_final("Administrador", "Brian", "Hernandez", "brian@gmail.com" , "1234", "12345678")
licas.agregar_final("Terror", "El conjuro", "James Wan", "2013", "12/12/2020", "12:00")
licas.agregar_final("Terror", "El conjuro 2", "James Wan", "2016", "12/12/2020", "12:00")
licas.agregar_final("Terror", "El conjuro 3", "James Wan", "2019", "12/12/2020", "12:00")
licas.agregar_final("Terror", "El conjuro 4", "James Wan", "2022", "12/12/2020", "12:00")
while True:
    print("===== MENÚ =====")
    print("1. Inicio de secion")
    print("2. Mostrar usuarios")
    print("3. Registrar usuarios")
    print("4. Ver las peliculas")
    print("5. Ver las salas")
    print("6.Comprar boletos")
    print("7. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        #Inicio de sesion

        correo = input("Ingrese su correo: ")
        contraseña = input("Ingrese su contraseña: ")
        if lista.Inicio_Session(correo, contraseña):
            print("Inicio de sesión exitoso")
        else:
            print("Correo o contraseña incorrectos")
    elif opcion == "2":
        #Ver los usuarios registrados
        lista.EscribirArchivo()
    elif opcion == "3":
        #Registro de usuarios
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        correo = input("Ingrese su correo: ")
        contraseña = input("Ingrese su contraseña: ")
        telefono = input("Ingrese su telefono: ")
        lista.agregar_final("Cliente" ,nombre, apellido, correo, contraseña, telefono)
    elif opcion == "4":
        #Ver las peliculas
        licas.Mostrar()
    elif opcion == "5":
        #ver las salas 
        nombre = input("Ingrese el nombre de la sala: ")
        numero = (input("Ingrese el número de la sala: "))
        asientos = (input("Ingrese el número de asientos: "))
        listasalas.agregar_final(nombre, numero, asientos)
        print("Sala agregada al final.")
        
    elif opcion == "6":
        listasalas.escribir_archivo("salas_cine.xml")

    elif opcion == "7":
        print("Feliz dia")
        break    
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
