import os 

def WriteInFile(Number):
    fobj = open("Number.txt","a")
    fobj.write(str(Number)+"\n")
    fobj.close()

def main():
    print("Enter 10 numbers that you want to add in the file :")
    i = 0
    while(i < 10):
        number = int(input())

        WriteInFile(number)

        i = i + 1

if __name__ == "__main__":
    main()