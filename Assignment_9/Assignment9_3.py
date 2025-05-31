import multiprocessing


def Factorial(value):
    fact = 1
    for i in range(1, value+1):
        fact = fact * i
    return fact



def main():
    InData = [5,10,11,21,50,100,150,220,300,500]
    p1 = multiprocessing.Pool()
    ret = p1.map(Factorial, InData)
    p1.close()
    p1.join()
    print(ret)

if __name__ == "__main__":
    main()
