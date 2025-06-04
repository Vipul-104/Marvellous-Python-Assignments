class Demo:
    value = 111

    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B

    def Fun(self):
        print("Inside the Fun :")
        print("The Value of First No is:",self.no1)
        print("The Value of Second No is:",self.no2)

    def Gun(self):
        print("Inside the Gun :")
        print("The Value of First No is:",self.no1)
        print("The Value of Second No is:",self.no2)

   

def main():
    print(" Value of Class Variable :",Demo.value)

    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()