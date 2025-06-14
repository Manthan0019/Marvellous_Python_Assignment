import os 

def ReadFile():
    fobj = open("Data.txt","r")
    content = fobj.read()
    fobj.close()
    
    return content
    
def main():
    Ret = ReadFile()
    print("Content from file : \n",Ret)

if __name__ == "__main__":
    main()