Ans = 1
i = 1
def Power(no1, no2):
    global Ans
    global i
    if(i <= no2):
        Ans = Ans * no1
        i = i + 1
        Power(no1,no2)

    return Ans

def main():

    print("Enter the number and the Power : ")
    value1 = int(input())
    value2 = int(input())

    ret =  Power(value1,value2)
    print(ret)



if __name__ == "__main__":
    main()