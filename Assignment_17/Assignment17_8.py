import time
import os
import schedule
import datetime

def ChkMail():
    print("Checking mail....")

def main():
    schedule.every(10).seconds.do(ChkMail)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()