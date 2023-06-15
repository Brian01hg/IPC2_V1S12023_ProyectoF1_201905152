from Lista_usuarios import Lista_usuarios
from Lista_Circular import ListaDoblementeCircularCategoria
from ListaDoble import ListaDobleCines
cines = ListaDobleCines()
lista = Lista_usuarios()
licas = ListaDoblementeCircularCategoria()
global numero_licas
contador_categorias = 0
lista.agregar_final("Administrador", "Brian", "Hernandez", "brian@gmail.com" , "1234", "12345678")
licas.agregar_final("Terror, Conjuro 2, James Wan, 2016, 19/06/2023, 16:00")
while True:
    # Segun las opciones de abajo en los elif, corregir el menu
    print("1. Iniciar sesión")
    print("2. Ver usarios XML")
    print("3. Agregar usuario")
    print("4. Modificar usuarios")
    print("5. Eliminar usuario")
    print("6. Mostrar Peliculas")
    print("7. Agregar Pelicula")
    print("8. Eliminar Peliculas")
    print("9. Modificar Peliculas")
    print("10. Mostrar Peliculas xml")
    print("11. Agregar Cine")
    print("12. Mostrar salas xml")
    print("13. Salir")
    
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        correo = input("Ingrese su correo: ")
        contraseña = input("Ingrese su contraseña: ")
        if lista.Inicio_Session(correo, contraseña):
            print("Inicio de sesión exitoso")
        else:
            print("Correo o contraseña incorrectos")
    elif opcion == "2":
        lista.EscribirArchivo()
    elif opcion == "3":
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        correo = input("Ingrese su correo: ")
        contraseña = input("Ingrese su contraseña: ")
        telefono = input("Ingrese su telefono: ")
        lista.agregar_final("Cliente" ,nombre, apellido, correo, contraseña, telefono)
    elif opcion =="4":
        print("Modificar Usuario")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        correo = input("Ingrese su correo: ")
        contraseña = input("Ingrese su contraseña: ")
        telefono = input("Ingrese su telefono: ")
        lista.ModificarPorCorreo(correo, nombre, apellido, contraseña, telefono)
        print("Usuario modificado con exito")
    elif opcion == "5":
        print("Eliminar Usuario")
        correo = input("Ingrese el correo del usuario: ")
        lista.eliminarPorCorreo(correo)
        print("Usuario eliminado con exito")
    elif opcion == "6":
        licas.Mostrar()
    elif opcion == "7":
        print("Agregar Pelicula")
        categoria = input("Ingrese la categoria de la pelicula: ")
        licas.agregar_final(categoria)
        contador_categorias = contador_categorias + 1
        numero_de_peliculas_a_agregar = int(input("Ingrese el numero de peliculas a agregar: "))
        numero_licas = numero_de_peliculas_a_agregar
        for i in range(numero_de_peliculas_a_agregar):
            titulo = input("Ingrese el titulo de la pelicula: ")
            director = input("Ingrese el nombre del director: ")
            año = input("Ingrese el año de la pelicula: ")
            fecha = input("Ingrese la fecha de la pelicula: ")
            hora = input("Ingrese la hora de la pelicula: ")
            licas.AgregarPelicula(categoria,titulo, director, año, fecha, hora)
            print("Pelicula agregada con exito")
        print("Pelicula agregada con exito")
    elif opcion == "8":
        print("Eliminar Pelicula")
        nombre = input("Ingrese el nombre de la pelicula: ")
        licas.EliminarCategoria(nombre)
        print("Pelicula eliminada con exito")
    elif opcion == "9":
        print("Modificar Pelicula")
        nombre = input("Ingrese el nombre de la pelicula: ")
        director = input("Ingrese el nombre del director: ")
        año = input("Ingrese el año de la pelicula: ")
        fecha = input("Ingrese la fecha de la pelicula: ")
        hora = input("Ingrese la hora de la pelicula: ")
        categoria = input("Ingrese la categoria de la pelicula: ")
        titulo = input("Ingrese el titulo de la pelicula: ")
        licas.ModificarPelicula(nombre, categoria, titulo, director, año, fecha, hora)
        print("Pelicula modificada con exito")    
    elif opcion == "10":
        print("Escribir archivo de peliculas")
        licas.EscribirXmlConBreak(numero_licas,contador_categorias)
    elif opcion == "11":
        print("Agregar Cine")
        nombre = input("Ingrese el nombre del cine: ")
        cines.append(nombre)
        print("Cine agregado con exito")
        numeros_de_salas_a_agregar = input("Ingrese el numero de salas a agregar: ")
        for i in range(int(numeros_de_salas_a_agregar)):
            numero = input("Ingrese el numero de la sala: ")
            asientos = input("Ingrese el numero de asientos: ")
            cines.AgregarSala(nombre, numero, asientos)
            print("Sala agregada con exito")
    elif opcion == "12":
        cines.EscribirArchivo()
    elif opcion == "13":
        print("Feliz dia")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
