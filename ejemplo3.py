class Circle: #definiendo la clase

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
      pi = 3.14 # (Will hardcode pi in this example)
      circumferenceValue = pi * int(self.radius) * 2
      return circumferenceValue

    def printCircumference(self):
      myCircumference = self.circumference()
      print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))
    
    def Area(self):
        pi = 3.14
        AreaValue = pi * int(self.radius) ** 2
        return AreaValue

    def printArea(self):
        myArea = self.Area()
        print("Area of a circle with a radius of " + str(self.radius)+ " is "+ str(myArea))

  
#circle1 = Circle(8) #instancia o creacion de objeto
##circle1.printArea() # metodo o un comportamiento.

##print("------------------------------------------------------")

#circle2 = Circle(10) #instancia o creacion de objeto
#circle2.printArea()







#radius1 = 2
#radius2 = 5
#radius3 = 7
# Since Circle is a class, it must be instatiated
# with the value of the radius first.
#circle1 = Circle(radius1)
#circle1.printArea()
