
ChkEven = lambda no : (no % 2 == 0)
Square = lambda no : (no ** 2)
Addition = lambda A,B : (A + B)




def filterX(Task, value):
    Result = []

    for no in value:
        ret = Task(no)
        if(ret == True):
            Result.append(no)

    return Result


def mapX(Task, value):
    Result = []
    for no in value:
        ret = Task(no)
        Result.append(ret)
    return Result


def reduceX(Task, value):
    Result = 0

    for no in value:
     Result= Task(Result, no)
    return Result



def main():
    Data = []

    print("Enter the size of list:")
    size = int(input())

    print("Enter the Numbers: ")
    for i in range(size):
        no = int(input())
        Data.append(no)
    print("Entered Data:",Data)

    FData = list(filterX(ChkEven, Data))
    print("The Filtered Data is :",FData)

    MData = list(mapX(Square, FData))
    print("The Map Data is:  ",MData)

    RData = reduceX(Addition, MData)
    print("Final Output: ",RData)


if __name__ == "__main__":
    main()