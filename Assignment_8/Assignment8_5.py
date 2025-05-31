import threading

def Display1():
    for i in range(1,51):
        print (i, end= " ")
    print()
    

def Display2():
    for i in range(50,0,-1):
        print (i, end = " ")
    print()
    
def main():
    dis1 = threading.Thread(target=Display1)
    dis1.start()
    dis1.join()


    dis2 = threading.Thread(target=Display2)
    dis2.start()
    dis2.join()


if __name__ == "__main__":
    main()