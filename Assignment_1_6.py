
def ChkNo(num):

    if(num>0):
        print("The Number is Positive")

    elif(num<0):
        print("The Number is Negative")

    else:
        print("its a 0")

def main():
    print("Enter the No :")
    No = int(input())

    ChkNo(No)



if __name__ == "__main__":
    main()