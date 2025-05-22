def PrintPattern(value):
    for i in range(value):
        for j in range(value):
            if (j<=i):
                print("*", end = " ")
        print()

def main():

    print("Enter the Number:")
    no = int(input())

    PrintPattern(no)
   
if __name__ == "__main__":
    main()