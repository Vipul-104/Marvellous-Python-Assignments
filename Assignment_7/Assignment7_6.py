def CheckPrime(value):
    count = 0
    for i in range(1, value+1):
        if((value % i) == 0):
            count = count + 1
        
    if (count <= 2):
        return True
    else:
        return False




def main():
    print("Enter the size of List :")
    size = int(input())

    data = []

    print("Enter The numbers :")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("The Entered list is :",data)

    Fdata = list(filter(CheckPrime, data))
    print("The Fitered data of Prime numbers is: ",Fdata)

if __name__ == "__main__":
    main()