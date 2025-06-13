import os

def ReadFile(Name):
    Ret = os.path.exists(Name)

    if(Ret == True):
       fobj = open(Name,"r")
       Content = fobj.read()
       fobj.close()
       return Content
    else:
        return("There is no such file.")
        
def main():
    print("Enter file that you eant to read :")
    FileName = input()

    ret = ReadFile(FileName)

    print("The content from file is : ",ret)

if __name__ == "__main__":
    main()