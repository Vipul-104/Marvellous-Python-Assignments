fact = 1
def Factorial(value):
    global fact
    if(value >= 1):
        fact = fact * value
        value = value - 1
        Factorial(value)
    return fact
        

def main():
    print("Enter the number:")
    no = int(input())

    ret = Factorial(no)
    print("The Factorial is : ",ret)

if __name__ == "__main__":
    main()