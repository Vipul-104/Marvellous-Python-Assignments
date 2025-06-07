class Calculator:
    def __init__(self):
        print("Enter The Fisrt No:")
        self.No1 = int(input())
        print("Enter The Second No:")
        self.No2 = int(input())


    def Addition(self):
        self.Add = self.No1 - self.No2

    def Substraction(self):
        self.Sub = self.No1 - self.No2

    def Multiplication(self):
        self.Multi = self.No1 * self.No2

    def Division(self):
        self.Div= self.No1 / self.No2

    def Display(self):
        print("The Addition Is:",self.Add)
        print("The Substraction Is:",self.Sub)
        print("The Multiplication Is:",self.Multi)
        print("The Division is:",self.Div)



def main():
    obj1 = Calculator()
    obj1.Addition()
    obj1.Substraction()
    obj1.Multiplication()
    obj1.Division()
    obj1.Display()


if __name__ == "__main__":
    main()