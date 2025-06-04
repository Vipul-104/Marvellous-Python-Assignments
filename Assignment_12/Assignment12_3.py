class Arithmatic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0  

    def Accept(self,No1,No2):
        self.Value1 = No1
        self.Value2 = No2

    def Addition(self):
        Result = self.Value1 + self.Value2
        return Result

        
    def Substraction(self):
        Result = self.Value1 - self.Value2
        return Result
        
    def Multiplication(self):
        Result = self.Value1 * self.Value2
        return Result
        
    def Division(self):
        Result = self.Value1 / self.Value2
        return Result
        
def main():
   print("Enter the First No: ")
   no1 = int(input())

   print("Enter the First No: ")
   no2 = int(input())

   Obj1 = Arithmatic()
   Obj1.Accept(no1,no2)

   Ret = Obj1.Addition()
   print("The Addition is :",Ret)

   Ret = Obj1.Substraction()
   print("The Substraction is :",Ret)

   Ret = Obj1.Multiplication()
   print("The Multiplication is :",Ret)

   Ret = Obj1.Division()
   print("The Division is :",Ret)

   print("___________________________________")

   print("Enter the First No: ")
   no1 = int(input())

   print("Enter the First No: ")
   no2 = int(input())

   Obj2 = Arithmatic()
   Obj2.Accept(no1,no2)

   Ret = Obj2.Addition()
   print("The Addition is :",Ret)

   Ret = Obj2.Substraction()
   print("The Substraction is :",Ret)

   Ret = Obj2.Multiplication()
   print("The Multiplication is :",Ret)

   Ret = Obj2.Division()
   print("The Division is :",Ret)

if __name__ == "__main__":
    main()