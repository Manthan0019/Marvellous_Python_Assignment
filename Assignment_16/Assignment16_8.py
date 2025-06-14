import os 

def RemoveBlankSpaces(Filename):
    if os.path.exists(Filename):
        fobj = open(Filename, "r")
        content = fobj.read()
        fobj.close()

        ContentWithoutSpace = content.replace(" ","")

        fobj = open(Filename,"w")
        fobj.write(ContentWithoutSpace)
        fobj.close()
    else:
        return "File does not exist."

def main():
    print("Enter file name :")
    filename = input()

    RemoveBlankSpaces(filename)

if __name__ == "__main__":
    main()