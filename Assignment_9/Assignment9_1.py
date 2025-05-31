import threading
import time

def Display1():
    for i in range(1, 6):
        time.sleep(1)
        print(i, end = " ")
    print()

def Display2():
    for i in range(1, 6):
        time.sleep(1)
        print(i, end = " ")
    print()


def Display3():
    for i in range(1, 6):
        time.sleep(1)
        print(i, end = " ")
    print()

def main():
    T1 = threading.Thread(target = Display1)
    T1.start()
    T1.join()

    T2 = threading.Thread(target = Display2)
    T2.start()
    T2.join()

    T3 = threading.Thread(target = Display3)
    T3.start()
    T3.join()
    

if __name__ == "__main__":
    main()