from functools import reduce


Product = lambda A,B : A*B

def main():
    print("Enter the size:")
    size = int(input())

    data = []

    print("Enter the Numbers : ")
    for no in range(size):
        no = int(input())
        data.append(no)

    print("The data is :",data)

    Rdata = reduce(Product, data)
    print("The Reduced data is: ",Rdata)

if __name__ == "__main__":
    main()
