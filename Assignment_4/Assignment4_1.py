# Lambda Function Which accepts parameters and return the Value in order of power of two

GetPower = lambda no : (no ** 2)

def main():
    print("Enter The number :")
    no = int(input())

    ret = GetPower(no)
    print("The power of",no,"is : ",ret)


if __name__ == "__main__":
    main()
