def StudentFile(StudentName):
    fobj = open("Student.txt","a")

    fobj.write("Student Name :"+StudentName+"\n")

    fobj.close()
    
def main():
    i = 0
    while(i < 5):
        print("Enter name of Student : ")
        name = input()
        StudentFile(name)
        i = i + 1

if __name__ == "__main__":
    main()