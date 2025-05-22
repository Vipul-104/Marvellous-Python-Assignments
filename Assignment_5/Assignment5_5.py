def CheckEven(value):
    if (value % 2 == 0):
        return True

    
    
def main():
    print("Enter the number: ")
    no = int(input())

    ret = CheckEven(no)
    if ret == True:
        print("The number is Even")

    else:
        print("The number is Odd")
        

if __name__ == "__main__":
    main()