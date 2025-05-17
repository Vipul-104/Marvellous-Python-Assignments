def Factorial(Value):
    fact = 1


    for i in range(1,Value+1):
        fact = fact * i
    return fact
    
    
    
def main():

    print("Enter the Number: ")
    No = int(input())

    Ret = Factorial(No)
    print("The Factorial Of the No is : ",Ret)



if __name__ == "__main__":
    main()