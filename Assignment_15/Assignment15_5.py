import os
import sys

def CountFrequency(FileName,StringValue):
    if(os.path.exists(FileName)==True):
        obj = open(FileName,"r")
        FileContent = obj.read()
        obj.close()

        count = 0
        i = 0

        while(i <= len(FileContent) - len(StringValue)):
            if(FileContent[i:i+len(StringValue)] == StringValue):
                count = count + 1
            i = i + 1
        return count

    else:
        print("There are no such files")

        
def main():
    if(len(sys.argv)==3):
        Ret = CountFrequency(sys.argv[1],sys.argv[2])
        print("The frequency is : ",Ret)
    else:
        print("Use this program as ProgramName.py FirstFileName.txt String")
if __name__ == "__main__":
    main()