
def Display(Value):
    for i in range(Value):
        for j in range(Value):
            if (i <= j) :
                print("*",end=" ")
        print()


def main():

    print("Enter the Number: ")
    No = int(input())

    Display(No)



if __name__ == "__main__":
    main()