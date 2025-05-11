def ChkNum(Value):
    if(Value % 2 == 0):
        return True
    
    else:
        return False


def main():
    print("Enter the Number : ")
    No = int(input())
    
    ret = ChkNum(No)

    if (ret == True):
        print("Its an Even Number..")

    else:
        print("Its an Even Number..")


if __name__ == "__main__":
    main()