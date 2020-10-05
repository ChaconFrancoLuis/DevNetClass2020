

def circumference(radius):
  pi = 3.14 # (Will hardcode pi in this example)
  circumferenceValue = pi * radius * 2
  return circumferenceValue

def printCircumference(radius):
  myCircumference = circumference(radius)
  print ("Circumference of a circle with a radius of " + str(radius) + " is " + str(myCircumference))


def forArea(radius):
    pi = 3.14
    miArea = pi * radius **2
    return miArea

def MostrarArea(radius):
    mostrar = forArea(radius)
    print("The area of a circle with a radius of " + str(radius) + " is " + str(mostrar))



#################################################3333

radius1 = int(input("agregar radio: "))


MostrarArea(radius1)