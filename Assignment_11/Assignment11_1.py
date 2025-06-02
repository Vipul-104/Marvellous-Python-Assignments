i = 1
def Display(no):
    global i
    if(i <= no):
        print(i, end = " ")
        i += 1
        Display(no)    

def main():
    print("Enter The Number :")
    No = int(input())
    Display(No)

if __name__ == "__main__":
    main()

