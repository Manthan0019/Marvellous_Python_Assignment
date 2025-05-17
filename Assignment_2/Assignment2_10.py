def SumDigit(Value):
    Sum = 0
    if(Value < 0):
        Value = -Value
    while(Value > 0):
        digit = Value % 10
        Sum = digit + Sum
        Value = int(Value / 10)
    return Sum

def main():
    print("Enter a number : ")
    No = int(input())

    result = SumDigit(No)

    print("Sum of digit is : ",result)

if __name__ == "__main__":
    main()