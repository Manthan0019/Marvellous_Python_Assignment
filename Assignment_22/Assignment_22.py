import time
import sys
import schedule
from Automation import *
    

def main():
    print("Enter email of reciver : ")
    reciverMail = input()

    sender = "manthansasane1122@gmail.com"
    senderpassword = "uohr cgtc tvtw yild"

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
           print("This is the script used for deletion of duplicate of files from a specific directory and generation of log file of that.")
        elif(sys.argv[1]=="--h" or sys.argv[1]=="--U"):
           print("Used this program as ScriptName.py DirectoryName TimeIntervalInMunites")
    elif(len(sys.argv)== 3):
        schedule.every(int(sys.argv[2])).minutes.do(DeleteDuplicate,reciverMail,sender,senderpassword,Path=sys.argv[1])

        while(True):
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Use --h for help and --u for usage")

    
if __name__ == "__main__":
    main()