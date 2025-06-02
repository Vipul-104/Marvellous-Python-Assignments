count = 0

def CountZeros(value):
    global count
    digit = -1
    while(value > 0):
        digit  = int(value % 10)
        print(digit)
        if(digit == 0):
            count = count + 1
        value = int(value / 10)
    return count

def main():
    print("Enter the Number :")
    no = int(input())

    ret = CountZeros(no)
    print("Zero Count Is is:",ret)

    
if __name__ == "__main__":
    main()