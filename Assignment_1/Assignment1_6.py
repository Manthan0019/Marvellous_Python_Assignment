def ChkNum(Value):
    Num = Value
    if (Num > 0 ):
        print("Positive number")
    elif(Num == 0):
        print("Zero")
    else:
        print("Negative number")

def main():
    print("Enter a Number : ")
    No = int(input())

    ChkNum(No)

if __name__ == "__main__":
    main()