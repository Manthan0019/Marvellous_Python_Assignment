def ChkNum(Value):
    Num = Value
    if(Num % 5 == 0):
        return True
    else:
        return False
    
def main():
    print("Enter a number : ")
    No = int(input())

    Ans = ChkNum(No)

    print(Ans)

if __name__ == "__main__":
    main()