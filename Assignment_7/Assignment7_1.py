CalSquare = lambda no : no ** 2
CalCube = lambda no : no ** 3

def main():

    print("Enter The Number: ")
    no = int(input())

    ret = CalSquare(no)
    print("The Square of the number: ",ret)

    ret1 = CalCube(no)
    print("The Cube of the number: ",ret1)




if __name__ == "__main__":
    main()