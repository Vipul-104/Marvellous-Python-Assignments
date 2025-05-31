import threading

def SumEvenFactors(value):
    sum = 0
    for i in range(value, value+1):
        if ((value % i) == 0):
            if((i % 2) == 0):
                sum = sum + i
    print("Sum Odf The Even Factors is :", sum)      

def SumOddFactors(value):
    sum = 0
    for i in range(value, value+1):
        if (value % i == 0):
            if(i % 2 != 0):
                sum = sum + i
    print("Sum Odf The Even Factors is :", sum)             
    

def main():

    print("Enter The Number:")
    no = int(input())

    EvenFactors = threading.Thread(target = SumEvenFactors, args = (no,))
    EvenFactors.start()
    EvenFactors.join()

    OddFactors = threading.Thread(target = SumOddFactors, args = (no,))
    OddFactors.start()
    OddFactors.join()


if __name__ == "__main__":
    main()


