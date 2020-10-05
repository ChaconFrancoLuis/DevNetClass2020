class mujer:

    def __init__(self):
        self.sexo = "femenino"
        print("soy un ente de la clase Mujer")

    def hablar(self,habla):
        print(habla)

    def caminar(self):
        print("Ahora se caminar y me voy caminando")

    def correr(self):
        print("ahora se correr y me voy corriendo")

class hombre:
    def __init__(self):
        self.sexo="masculino"
        print("soy un objeto de la clase hombre")

    def hablar(self,habla):
        print(habla)

    def caminar(self):
        print("ahora se caminar y voy caminando")

    def correr(self):
        print("ahora se correr.....")


persona2 = hombre()
persona2.hablar("Mi nombre es Fernando")
persona2.correr()
print(persona2.__dict__)

print("---------------------------")

persona1 = mujer()
persona1.hablar("Mi nombre es Rebecca")
persona1.caminar()
print("mi sexo es: ",persona1.sexo)
print(persona1.__dict__)


    