import time
import datetime
import schedule

def DisplayDateTime():
    ret = datetime.datetime.now()
    print("Current Date Time : ",ret)

def main():
    schedule.every(1).minute.do(DisplayDateTime)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()