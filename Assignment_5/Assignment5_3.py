def CheckAge(Value):
    if (Value >= 18):
        return True

def main():
    print("Enter Your Age : ")
    Age = int(input())

    ret = CheckAge(Age)
    if ret == True:
        print("You Are eligible for Voting...")

    else:
        print("You Are Not eligible for voting...")

if __name__ == "__main__":
    main()