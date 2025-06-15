import os
import schedule
import time
import datetime


def DiplayLunch():
    print("Lunch Time!!")

def DiplayWrapup():
    print("Wrap up Work!!")

def main():
    print("This Program Will Display Tasks!!")
    
    schedule.every().day.at("13:00").do(DiplayLunch)
    schedule.every().day.at("18:00").do(DiplayWrapup)


    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()