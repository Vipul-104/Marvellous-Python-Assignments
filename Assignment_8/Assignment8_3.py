import threading

def AddEven(value):
    sum = 0
    for i in range(len(value)):
        if (value[i] % 2 == 0):
            sum = sum + value[i]
    print("The Sum of Even Elemnts is :",sum)


def AddOdd(value):
    sum = 0 
    for i in range(len(value)):
        if ((value[i] % 2) != 0):
            sum = sum + value[i]
    print("The Sum Odf Odd Elemnts is :",sum)


def main():
    print("Enter the Size of the elements:")
    size = int(input())

    data = []
    print("Enter The Elements : ")
    for no in range(size):
        no = int(input())
        data.append(no)
    print("Entered Data is: ",data)

    addEven = threading.Thread(target = AddEven, args=(data,))
    addEven.start()
    addEven.join()

    addOdd = threading.Thread(target = AddOdd, args= (data,))
    addOdd.start()
    addOdd.join()

if __name__ == "__main__":
    main()