
sum = 0

def DigitAdd(value):
    global sum
    if(value > 0):
        digit  = value % 10
        print(digit)
        sum = sum + digit
        value= int(value / 10)
        DigitAdd(value)
    return sum

def main():
    print("Enter the Number :")
    no = int(input())

    ret = DigitAdd(no)
    print("Summetion is:",ret)

    
if __name__ == "__main__":
    main()