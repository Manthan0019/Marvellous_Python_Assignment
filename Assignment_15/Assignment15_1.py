import os

def ChkFile(Name):
    Ret = os.path.exists(Name)
    return Ret


def main():
    print("Enter file name : ")
    filename = input()

    ret = ChkFile(filename)
    if(ret == True):
        print(filename,"This file exists.")
    else:
        print("The file does not exists.")

if __name__ == "__main__":
    main()