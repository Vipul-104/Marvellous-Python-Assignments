i = 0

def Display(value):
    global i

    if(i < value):
        j = 0
        while(j < value and j<= i):
            print("*",end = " ")
            j = j + 1
        print()
        i = i+1
        Display(value)

def main():
    print("Enter the no: ")
    no = int(input())

    Display(no)

if __name__ == "__main__":
    main()