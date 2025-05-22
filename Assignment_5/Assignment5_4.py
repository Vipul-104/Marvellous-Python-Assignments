def CheckMax(value1,value2,value3):
    if(value1 > value2):
        if(value1 > value3):
           return value1
        else :
            return value2
    else:
        return value3
        
    

def main():
    print("Enter the first no:")
    No1 = int(input())

    print("Enter the second no:")
    No2 = int(input())

    print("Enter the Third no:")
    No3 = int(input())

    ret = CheckMax(No1,No2,No3)
    print("The largest no is:",ret)


if __name__ == "__main__":
    main()