import time
import multiprocessing
import threading

def Sum():
    sum = 0
    for i in (1, 10000001):
        sum = sum + i
    print("The Summation is :",sum)


def main():
    start_time=time.time()
    Sum()
    end_time = time.time()
    Function_time = end_time - start_time

    #threading
    start_time = time.time()
    t1 = threading.Thread(target = Sum)
    t1.start()
    t1.join()
    end_time = time.time()
    Threading_time = end_time - start_time

    #multprocessing
    start_time = time.time()
    P1 = multiprocessing.Process(target = Sum)
    P1.start()
    P1.join()
    end_time = time.time()
    Processinging_time = end_time - start_time

    print("The time required for normal Function:",Function_time)
    print("The time required for MultiThreading:",Threading_time)
    print("The time required for MultiProcessing:",Processinging_time)


if __name__ == "__main__":
    main()