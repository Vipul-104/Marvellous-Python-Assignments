import multiprocessing.process
import os
import multiprocessing
import time


def Square(value):
    print("The PID is : ",os.getpid())
    print("The PPID is : ",os.getppid())
    for i in value:
        print(i ** 2)

def main():
    listInput = [10000,20000,30000,40000]

    p1 = multiprocessing.Process(target = Square, args = (listInput,))
    p1.start()
    p1.join()




if __name__ == "__main__":
    main()