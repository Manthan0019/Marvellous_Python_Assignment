import os
import sys

def CompareContent(FirstFileName,SecondFileName):
    if(os.path.exists(FirstFileName)==True and os.path.exists(SecondFileName)==True):
        obj = open(FirstFileName,"r")
        FirstFileContent = obj.read()
        obj.close()

        obj1 = open(SecondFileName,"r")
        SecondFileContent = obj1.read()
        obj1.close()

        if(FirstFileContent == SecondFileContent):
            return True
        else:
            return False
        
    else:
        print("There are no such files")

        
def main():
    if(len(sys.argv)==3):
        Ret = CompareContent(sys.argv[1],sys.argv[2])
        if(Ret == True):
            print("Success! The content from both the files is same")
        else:
            print("Failure! The content from both file is not same")
    else:
        print("Use this program as ProgramName.py FirstFileName.txt SecondFileName.txt")
if __name__ == "__main__":
    main()