import os 

def CreateFile(Name, Marks):   
    fobj = open("Marks.txt", "w")
    fobj.write("Student Name: " + Name + "\n")
    fobj.write("Marks : " + str(Marks) + "\n")
    fobj.close()  

def ReadFile():
    if os.path.exists("Marks.txt"):
        fobj = open("Marks.txt", "r")
        content = fobj.read()
        fobj.close()
        return content
    else:
        return "File does not exist."

def main():
    print("Enter student name :")
    name = input()

    print("Marks obtained by student :")
    marks = int(input())

    CreateFile(name, marks)

    Ret = ReadFile()

    print("Content from file:\n", Ret)

if __name__ == "__main__":
    main()
