def ChkNum(Value):
    No = Value

    if (No % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("Enter a number : ")

    No1 = int(input())
    ChkNum(No1)

if __name__ == "__main__":
    main()