def CalPeri(value1, value2):
    Perimeter = (2*value1) + (2*value2)
    return Perimeter


def CalArea(value1, value2):
    Area = (value1 * value2)
    return Area


def  main():
    print("Enter the Length of rectangle : ")
    ln = int(input())

    print("Enter the Width of rectangle : ")
    wid = int(input())

    ret1 = CalPeri(ln,wid)
    print("The perimeter of Rectangle is: ",ret1)

    ret2 = CalArea(ln,wid)
    print("The perimeter of Rectangle is: ",ret2)

if __name__ =="__main__":
    main()