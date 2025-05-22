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
    print("Enter the Number : ")
    No = int(input())

    ret = CheckPrime(No)

    if ret == True:
        print("Its A prime Number")

    else:
        print("Its not a prime number")

if __name__ == "__main__":
    main()