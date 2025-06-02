

sum = 0

def Addition(value):
    global sum
    if(value >= 1):
        sum = sum + value
        value = value - 1
        Addition(value)
    return sum



def main():
    print("Enter the Number :")
    no = int(input())

    ret = Addition(no)
    print("Summetion is:",ret)

    


if __name__ == "__main__":
    main()