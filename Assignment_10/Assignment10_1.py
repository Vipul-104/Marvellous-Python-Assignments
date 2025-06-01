Power = lambda no : no **2


def main():
    print("Enter the Number:-")
    No = int(input())
    
    ret = Power(No)
    print("Power of",No,"is : ",ret)


if __name__ == "__main__":
    main()