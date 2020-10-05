class circle: #creacion de la clase
    radio = 0 # variable clase
    color = ""

    def circumferencia(self): #definicion de metodo
        return 3.14 * 2 * self.radio

    def pcircum(self):
        printea = self.circumferencia()
        print("el resultado es: ",printea)

    def Area(self):
        pi =  3.14
        AreaValue = pi * int(self.radio) ** 2
        return AreaValue

    def printArea(self):
        myArea = self.Area()
        print("el resultado de area es: ",myArea)

circulo1 = circle() # instancia o creacion de un objeto
circulo1.radio = 8 # variable de instancia
circulo1.color = "Verde"
circulo1.pcircum()
print(circulo1.__dict__)

print("------------------------------------------------------------------")

circulo2 = circle()
circulo2.radio = 10
circulo2.color = "Azul"
circulo2.pcircum()
print(circulo2.__dict__)







