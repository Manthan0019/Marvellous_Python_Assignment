import os
import time
import sys
import schedule
import shutil

def CopyFiles(SourceDirectory,DestinamtionDirectory):
    if not os.path.isabs(SourceDirectory):
        SourceDirectory = os.path.abspath(SourceDirectory)


    timestamp = time.ctime()
    logfilename = "Copyfilelog%s.log"%(timestamp)
    logfilename = logfilename.replace(" ","")
    logfilename = logfilename.replace("/","_")
    logfilename = logfilename.replace(":","_")

    fobj = open(logfilename,"w")

    if (os.path.isdir(SourceDirectory)):
        try:
            shutil.copytree(SourceDirectory, DestinamtionDirectory)
            fobj.write("All files Successfully copied")
        except FileExistsError:
            fobj.write("Error: Destination directory already exist")
        except Exception as e:
            fobj.write("An error occurred:"+e)
                       
    else:
        print("No such a directory")
        return
    fobj.close()

def main():
    if(len(sys.argv)==2):
        if(sys.argv[1]== "--u" or sys.argv[1]=="--U"):
            print("use this script as programname.py directoryName .Extention")
            exit()
        elif(sys.argv[1]== "--h" or sys.argv[1]=="--H"):
            print("This script is used for Display all file names with specific extention")
            exit()
    elif(len(sys.argv)==3):
        schedule.every(1).hours.do(CopyFiles,sys.argv[1],sys.argv[2])
        while(True):
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Enter valid input")

if __name__ == "__main__":
    main()