from functools import reduce

Even = lambda no : no % 2 == 0
CalSquare = lambda no : no ** 2
Addition = lambda A,B : A + B

def main():
    print("Enter the size of list:")
    size = int(input())

    data = []

    print("Enter the Elements: ")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("The Entered Elements Are :",data)

    Fdata = list(filter(Even, data))
    print("The Filtered Data is : ",Fdata)

    Mdata = list(map(CalSquare, Fdata))
    print("The Mapped Data is : ",Mdata)

    Rdata = reduce(Addition, Mdata)
    print("The Reduced Data is : ",Rdata)

if __name__ == "__main__":
    main()

