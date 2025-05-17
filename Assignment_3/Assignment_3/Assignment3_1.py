def AddData(Value):
    ans = 0 
    for num in (Value):
        ans =ans + num
    return ans

def main():
    print("Enter the Size:")
    size = int(input())

    data = list()

    print("Enter the Elements: ")
    for i in range(size):
        no = int(input())
        data.append(no)
    print(data)


    ret = AddData(data)
    print("Addition of the Elements is: ",ret)



if __name__ == "__main__":
    main()