from functools import reduce

RightData = lambda no : no >= 70 and no <= 90
Increase = lambda no : no + 10
Product = lambda A,B : A * B



def main():
    print("Enter the size of list:")
    size = int(input())

    data = []

    print("Enter the Elements: ")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("The Entered Elements Are :",data)

    Fdata = list(filter(RightData, data))
    print("The Filtered Data is : ",Fdata)

    Mdata = list(map(Increase, Fdata))
    print("The Mapped Data is : ",Mdata)

    Rdata = reduce(Product, Mdata)
    print("The Reduced Data is : ",Rdata)



if __name__ == "__main__":
    main()