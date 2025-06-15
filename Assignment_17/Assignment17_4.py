import os
import schedule
import time
import datetime


def Diplay():
    print("Namaskarr!!")

def main():
    print("This Program Will Print ..Namskar!!.. At 9:00 AM Everyday!!")
    
    schedule.every().day.at("09:00").do(Diplay)

    

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()