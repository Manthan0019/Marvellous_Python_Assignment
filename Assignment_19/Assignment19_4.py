import os
import time
import sys
import schedule
import shutil

def CopyFiles(SourceDirectory,DestinamtionDirectory,Extension):
    if not os.path.isabs(SourceDirectory):
        SourceDirectory = os.path.abspath(SourceDirectory)
    timestamp = time.ctime()
    logfilename = "Copyfilelog%s.log"%(timestamp)
    logfilename = logfilename.replace(" ","")
    logfilename = logfilename.replace("/","_")
    logfilename = logfilename.replace(":","_")

    fobj = open(logfilename,"w")

    if (os.path.isdir(SourceDirectory)):
        if not os.path.exists(DestinamtionDirectory):
            os.makedirs(DestinamtionDirectory)

        count = 0
        for FolderName, SubFolderName, FileName in os.walk(SourceDirectory):
            for fname in FileName:
                Fullfname = os.path.join(FolderName, fname)
                if(Fullfname.endswith(Extension)):
                    try:
                        shutil.copy2(Fullfname, os.path.join(DestinamtionDirectory, fname))
                        fobj.write(fname + "\n") 
                        count += 1
                    except Exception as e:
                        fobj.write("Error copying file: " + str(e) + "\n")

        if count == 0:
            fobj.write("No matching files found.\n")
                       
    else:
        print("No such a directory")
        return
    fobj.close()

def main():
    if(len(sys.argv)==2):
        if(sys.argv[1]== "--u" or sys.argv[1]=="--U"):
            print("use this script as programname.py souesedirectoryName destinationdirectoryName .Extention")
            exit()
        elif(sys.argv[1]== "--h" or sys.argv[1]=="--H"):
            print("This script is used for Copy all files with the specified extension from first directory into second directory.")
            exit()
    elif(len(sys.argv)==4):
        schedule.every(1).hours.do(CopyFiles,sys.argv[1],sys.argv[2],sys.argv[3])
        while(True):
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Enter valid input")

if __name__ == "__main__":
    main()