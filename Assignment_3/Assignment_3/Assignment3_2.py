def MaxNo(Value):
    max = Value[0]

    for num in Value:
        if(num > max):
            max = num
        else:
            num = max
    return max



def main():
    print("Enter the Size:")
    size = int(input())

    data = list()

    print("Enter the Elements: ")
    for i in range(size):
        no = int(input())
        data.append(no)
    print(data)


    ret = MaxNo(data)
    print("Max no in the Elements is: ",ret)



if __name__ == "__main__":
    main()