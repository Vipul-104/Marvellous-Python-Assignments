# FMR 1

Inbetween = lambda no : (no <= 90 and no>=70)
Increase = lambda no : (no + 1)
Product = lambda A,B : (A * B)


def filterX(Task, value):
    Result = []

    for no in value:
        ret = Task(no)
        if ret == True:
            Result.append(no)

    return Result

def mapX(Task, value):
    Result = []

    for no in value:
        ret = Task(no)
        Result.append(ret)

    return Result


def reduceX(Task, value):
    Result = 1
    
    for no in value:
        Result = Task(Result, no )

    return Result




def main():
    Data = []

    print("Enter the Size:")
    size = int(input())

    print("Enter the Numbers :")
    for i in range(size):
        no = int(input())
        Data.append(no)
    print("The Entered Data is:",Data)

    Fdata = list(filterX(Inbetween, Data))
    print("The Filtered Data is",Fdata)

    Mdata = list(mapX(Increase, Fdata))
    print("The Mapped Data is",Mdata)

    Rdata =reduceX(Product, Mdata)
    print("Output is",Rdata)


if __name__ == "__main__":
    main()