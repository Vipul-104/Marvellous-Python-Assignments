CheckEven = lambda A : A % 2 == 0





def main():
    print("Enter the size:")
    size = int(input())

    data = []

    print("Enter the Elements :")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("The Entered elemnts are",data)

    Rdata = list(filter(CheckEven, data))
    print("The Filtered Data of Even number is :",Rdata)




if __name__ == "__main__":
    main()