Doubleint = lambda X : X * 2



def main():

    print("Enter the Size of list:")
    size = int(input())
    data = []

    print("Enter the numbers:")
    for no in range(size):
        no = int(input())
        data.append(no)

    print("The Entered data is:",data)

    Mdata =list(map(Doubleint,data))
    print("The mapped data is:",Mdata)


if __name__ == "__main__":
    main()