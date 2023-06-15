class nodo_caracter:
    def __init__(self,caracter):
        self.caracter = caracter
        self.siguiente = None
class pila:
    def __init__(self): 
        self.cima = None
    def push(self,caracter):
        nuevoNodo = nodo_caracter(caracter)
        if(self.cima == None):
            self.cima = nuevoNodo
        else:
            nuevoNodo.siguiente = self.cima
            self.cima = nuevoNodo
    
    def pop(self):
        if(self.cima == None):
            return None
        else:
            aux = self.cima
            self.cima = self.cima.siguiente
            return aux.caracter

pila_ = pila()
entrada = "12+45-15*78/"
for i in entrada:
    if i == "+":
        primero = int(pila_.pop())
        segundo = int(pila_.pop())
        suma = primero + segundo
        print("Suma: ", suma)
    
    elif i == "-":
        primero = int(pila_.pop())
        segundo = int(pila_.pop())
        resta = primero - segundo
        print("Resta: ", resta)
    elif i == "*":
        primero = int(pila_.pop())
        segundo = int(pila_.pop())
        multiplicacion = primero * segundo
        print("Multiplicación: ", multiplicacion)
    elif i == "/":
        primero = int(pila_.pop())
        segundo = int(pila_.pop())
        division = primero / segundo
        print("División: ", division)
    pila_.push(i)
