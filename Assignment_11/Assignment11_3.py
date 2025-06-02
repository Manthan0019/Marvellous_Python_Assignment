Sum = 0 

def SumDigits(No):
    global Sum
    if (No != 0):
        digit = No % 10
        Sum = Sum + digit
        SumDigits(No // 10)
    return Sum

def main():
    print("Enter a number:")
    Value = int(input())

    Ret = SumDigits(Value)
    print("Sum of digits:", Ret)

if __name__ == "__main__":
    main()
