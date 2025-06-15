import os
import schedule
import time
import datetime


def Backup():
    print("Backup Completed..")
    fobj = open("backup_log.txt","a")
    data = time.asctime()
    fobj.write("Backup Done At: ")
    fobj.write(data)
    fobj.write("\n\n\n\n")
    fobj.close()
    print("running!!..have Patience")

def main():
    print("File Taking The Backup")
    fobj = open("backup_log.txt","w")
    fobj.close()
    
    schedule.every(1).hour.do(Backup)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()