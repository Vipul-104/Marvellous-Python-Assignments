def CheckPrime(Value):
    count = 0
    for i in range(1, Value+1):
        if Value % i == 0:
            count = count+1
        if(count > 2):
            return False
        else:
            return True




def main():
    print("Enter the no that you Want to check: ")
    No = int(input())

    Ret = CheckPrime(No)

    if Ret == True:
        print("The No is prime..")

    else:
        print("The No is not Prime..")



if __name__ == "__main__":
    main()