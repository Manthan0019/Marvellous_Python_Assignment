import time
import os
import schedule
import datetime

def CreateFile():
    if(os.path.exists("Marvellous.txt")):
        fobj = open("Marvellous.txt","a")
    else:
        fobj = open("Marvellous.txt","w")

    fobj.write("Current time = "+str(datetime.datetime.now()))

    fobj.close

def main():
    schedule.every(1).minutes.do(CreateFile)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()