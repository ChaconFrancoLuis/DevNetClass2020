class Carro:
    tipo ="Camioneta"


    def __init__(self,marca,color,modelo): #metodo constructor, inicializacion.
        self.marca=marca
        self.color=color
        self.modelo=modelo

    def Carro_movimiento(self):
        print("el carro se esta moviendo")

    def Carro_estacionado(self):
        print("el carro esta estacionado")

carro1 = Carro("toyota","plateado","2020") #instancia de la clase Carro. inicializo marca,color,modelo,tipo.
carro1.tipo = "Sedan"
print(carro1.__dict__)

carro1.Carro_movimiento()
carro1.Carro_estacionado()