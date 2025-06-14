import os 
import sys

def CopyContent(SourceFileName,DestinationFileName):   
    if(os.path.exists(SourceFileName)):
            fobj1 = open(SourceFileName,"r")
            Data1 = fobj1.read()

            fobj2 = open(DestinationFileName,"a")
            fobj2.write(Data1)
            
            fobj1.close()
            fobj2.close()

def main():
    if(len(sys.argv)):
        CopyContent(sys.argv[1],sys.argv[2])

    else:
         print("Use this program as ProgramFile.py sourceFile.txt,destinationfile")
if __name__ == "__main__":
    main()