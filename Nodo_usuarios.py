class Usuario:
    def __init__(self, rol ,nombre, apellido, correo, contraseña, telefono):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña
        self.telefono = telefono
        self.siguiente = None