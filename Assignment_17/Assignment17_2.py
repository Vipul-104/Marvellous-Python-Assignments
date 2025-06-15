import os
import schedule
import time
import datetime


def DispalyDatetime():
    print("Inside Automation Script,Current Time Is:",datetime.datetime.now())

def main():
    schedule.every(1).minutes.do(DispalyDatetime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()