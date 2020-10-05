class circle: #definiendo la clase

    def __init__(self,radio): #el constructor permite agregar argumentos o parametros con cada instancia.
        self.radio = radio
        self.ejemplo = "este es un ejemplo"

    def circumferencia(self): # self nos ayuda a hacer referencia al mismo metodo.
        return 3.14 * 2 * int(self.radio) #self nos ayuda a acceder a la variable radio.

    def pcircum(self): # definiendo el metodo
        printea = self.circumferencia()
        print("el resultado es: ",printea)


circulo1 = circle(8) #instancia de la clase circle.
circulo1.pcircum()
print(circulo1.__dict__)
