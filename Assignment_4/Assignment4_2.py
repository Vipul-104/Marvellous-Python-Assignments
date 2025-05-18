#lambda function for accepting two parameters and returns multiplication of it

Multiplication = lambda A,B : (A * B)

def main():

    print("Enter the 1st No :")
    No1 = int(input())


    print("Enter the 2nd No :")
    No2 = int(input())

    ret = Multiplication(No1, No2)
    print("The Multiplication is :",ret)


if __name__ == "__main__":
    main()