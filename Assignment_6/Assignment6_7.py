def CheckLargest(value):
    max = 0
    for i in range(len(value)):
        if max > value[i]:
            max = max

        else:
            max = value[i]

    return max




def main():

    print("Enter 5 number: ")
    data = []
    for i in range(5):
        no = int(input())
        data.append(no)
    
    print("Entered Numbers Are:",data)

    ret = CheckLargest(data)

    print("The Largest no is :",ret)
if __name__ == "__main__":
    main()