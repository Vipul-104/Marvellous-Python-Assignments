Ans = 0

def Sum(Value1, Value2):
    Ans = Value1 + Value2
    return Ans

def Difference(Value1, Value2):
    Ans = Value1 - Value2
    return Ans

def Product(Value1, Value2):
    Ans = Value1 * Value2
    return Ans

def Division(Value1, Value2):
    Ans = Value1 / Value2
    return Ans

def main():
    print("Enter the First No : ")
    No1 = int(input())
    print("Enter the Second No : ")
    No2 = int(input())
    
    ret1 = Sum(No1, No2)
    print("The Sum of Two Numbers is :",ret1)

    ret2 = Difference(No1, No2)
    print("The Difference of Two Numbers is :",ret2)

    ret3 = Product(No1, No2)
    print("The Product of Two Numbers is :",ret3)

    ret4 = Division(No1, No2)
    print("The Division of Two Numbers is :",ret4)

if __name__ == "__main__":
    main()

 