import os
import schedule
import time
import datetime


def DoDiplay():
    print("Do Coding!!:")

def main():
    print("Inside Automation Script,Current Time Is:",datetime.datetime.now())
    schedule.every(30).minutes.do(DoDiplay)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()