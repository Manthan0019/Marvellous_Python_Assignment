import os
import sys 
import psutil
import time
import schedule

def CreateLog():
    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace("/","_")
    timestamp = timestamp.replace(":","_")

    filename = "ProcessInfo%slog.log"%(timestamp)
    
    fobj = open(filename,"w")

    Border = ("-")*80
    fobj.write(Border)
    fobj.write("\n\t\tTihs is a cureent running process log file \n")
    fobj.write("\t\tThis log file is created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n")

    Data = ProcInfo()

    for value in Data:
        fobj.write("%s \n\n"%(value))
    
    fobj.write(Border)

    fobj.close()

def ProcInfo():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(info)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listprocess

def main():
    if(len(sys.argv)== 2):
        if(sys.argv[1]== "--h" or sys.argv[1]=="--H"):
            print("This is the automation script which displays information of running process.")
        elif(sys.argv[1]== "--u" or sys.argv[1]=="--U"):
            print("Use this script as ScriptName.py TimeInterval")
        else:
            schedule.every(int(sys.argv[1])).minutes.do(CreateLog)

            while(True):
                schedule.run_pending()
                time.sleep(1)
    else:
        print("please use --h for help and --u for usage")
        print("Please enter valid inputs")
if __name__ == "__main__":
    main()