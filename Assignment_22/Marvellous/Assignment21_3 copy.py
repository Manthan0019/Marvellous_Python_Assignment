import os
import sys 
import psutil
import time
import schedule

def CreateLog(FolderName,ProcessName):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace("/","_")
    timestamp = timestamp.replace(":","_")

    filename = os.path.join(FolderName,"ProcessInfo%slog.log"%(timestamp))
    
    fobj = open(filename,"w")

    Border = ("-")*80
    fobj.write(Border)
    fobj.write("\n\t\tTihs is a cureent running process log file \n")
    fobj.write("\t\tThis log file is created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n")

    Data = ProcInfo(ProcessName)

    for value in Data:
        fobj.write("%s \n\n"%(value))
    
    fobj.write(Border)

    fobj.close()

def ProcInfo(Processname):
    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            if(info['name']==Processname):
                listprocess.append(info)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listprocess

def main():
    if(len(sys.argv)== 2):
        if(sys.argv[1]== "--h" or sys.argv[1]=="--H"):
            print("This is the automation script which displays information of running process.")
        elif(sys.argv[1]== "--u" or sys.argv[1]=="--U"):
            print("Use this script as ScriptName.py DirectoryName ProcessName TimeInterval")
    elif(len(sys.argv)==4):
        schedule.every(int(sys.argv[3])).minutes.do(CreateLog,sys.argv[1],sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)
    else:
        print("please use --h for help and --u for usage")
        print("Please enter valid inputs")
if __name__ == "__main__":
    main()