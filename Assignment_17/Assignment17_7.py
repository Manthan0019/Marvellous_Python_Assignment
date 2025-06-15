import time
import os
import schedule
import datetime

def CreateFile():
    if(os.path.exists("Backup_log.txt")):
        fobj = open("Backup_log.txt","a")
    else:
        fobj = open("backup_log.txt","w")

    fobj.write("Current time = "+str(datetime.datetime.now()))

    fobj.close

def main():
    schedule.every(1).hours.do(CreateFile)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()