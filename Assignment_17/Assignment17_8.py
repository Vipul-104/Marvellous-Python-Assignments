import os
import schedule
import time
import datetime


def Dispaly():
    print("Checking mails...")

def main():
    print("Inside Automation Script,Current Time Is:",datetime.datetime.now())

    schedule.every(10).seconds.do(Dispaly)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()