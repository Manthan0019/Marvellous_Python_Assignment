import os
import sys

def CreateFile(FileName):
    if(os.path.exists(FileName)==True):
        obj = open(FileName,"r")
        OldContent = obj.read()
        obj.close()
    else:
        print("There is no such file")

    fobj = open("Demo.txt","w")
    fobj.write(OldContent)
    fobj.close()


        
def main():
    if(len(sys.argv)==2):
        CreateFile(sys.argv[1])
    else:
        print("Use this program as ProgramName.py FileName.txt")
if __name__ == "__main__":
    main()