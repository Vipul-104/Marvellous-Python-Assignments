class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area= 0.0
        self.Circumference = 0.0


    def Accept(self,Value1):
        self.Radius = Value1


    def CalculateArea(self):
        CArea = Circle.PI * self.Radius**2
        self.Area = CArea

    def CalculateCircumference(self):
        circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("The radius is : ",self.Radius)
        print("The Circumference is : ",self.Circumference)
        print("The Area is : ",self.Area)

def main():
    obj1 = Circle()
    obj1.Accept(14)
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    print("_______________________________")
        
    obj2 = Circle()
    obj2.Accept(28)
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()

    print("_______________________________")

    obj3 = Circle()
    obj3.Accept(49)
    obj3.CalculateArea()
    obj3.CalculateCircumference()
    obj3.Display()
        

if __name__ == "__main__":
    main()