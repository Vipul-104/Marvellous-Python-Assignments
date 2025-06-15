import os
import schedule
import time
import datetime


def WriteTime():
    fobj = open("Marvellous.txt","a")
    fobj.write("The Current Time is")
    fobj.write("\n")
    data = time.asctime()
    fobj.write(data)
    fobj.write("\n")
    fobj.close()
    print("running!!..have Patience")

def main():
    print("This Script will Write Current Time Into THe File After every 5 mins")
    fobj = open("Marvellous.txt","w")
    fobj.close()
    
    schedule.every(5).minutes.do(WriteTime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()