def MinNo(Value):
    min = Value[0]

    for num in Value:
        if(num < min):
            min = num
        else:
            num = min
    return min



def main():
    print("Enter the Size:")
    size = int(input())

    data = list()

    print("Enter the Elements: ")
    for i in range(size):
        no = int(input())
        data.append(no)
    print(data)


    ret = MinNo(data)
    print("Min no in the Elements is: ",ret)



if __name__ == "__main__":
    main()