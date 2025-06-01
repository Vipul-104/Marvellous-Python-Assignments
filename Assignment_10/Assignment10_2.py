Multiplication = lambda A,B :  A*B


def main():
    print("Enter the First Number:-")
    No1 = int(input())

    print("Enter the Second Number:-")
    No2 = int(input())
    
    ret = Multiplication(No1, No2)
    print("Multiplication is : ",ret)


if __name__ == "__main__":
    main()