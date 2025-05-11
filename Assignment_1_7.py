def ChkNum(Value):
    if(Value % 5 == 0):
        return True
    
    else:
        return False


def main():
    print("Enter the Number : ")
    No = int(input())
    
    ret = ChkNum(No)

    if (ret == True):
        print("The NUmber is Devisible by 5")

    else:
        print("Number is not divisible by 5")


if __name__ == "__main__":
    main()