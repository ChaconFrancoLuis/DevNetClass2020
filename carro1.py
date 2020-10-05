#Clase sin constructor.

class Carro: #creacion de la clase
    marca = ""
    color = ""
    modelo = "2020" #variable de clase
    tipo = ""

    def Carro_movimiento(self):
        print("el carro se esta moviendo")

    def Carro_estacionado(self):
        print("el carro esta estacionado")

carro1 = Carro()
carro1.marca = "Toyota"
carro1.color = "Negro"
carro1.tipo = "Camioneta"

print(carro1.__dict__)
carro1.Carro_movimiento()
carro1.Carro_estacionado()

carro2 = Carro()
carro3 = Carro()
