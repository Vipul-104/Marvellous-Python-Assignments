import Arithmatic



def main():
    print("Enter the 1st NO. : ")
    No1 = int(input())
    print("Enter the 2nd NO. : ")
    No2 = int(input())

    Ret1 = Arithmatic.Add(No1, No2)
    Ret2 = Arithmatic.Sub(No1, No2)
    Ret3 = Arithmatic.Multi(No1, No2)
    Ret4 = Arithmatic.Div(No1, No2)

    print("The addition of this Numbers :",Ret1)
    print("The Substraction of this Numbers :",Ret2)
    print("The Multiplication of this Numbers :",Ret3)
    print("The Division of this Numbers :",Ret4)
    


if __name__ == "__main__":
    main()