def Digit(Value):
    Count = 0
    if(Value < 0):
        Value = -Value
    while(Value > 0):
        Count = Count + 1
        Value = int(Value / 10)
    return Count

def main():
    print("Enter a number : ")
    No = int(input())

    result = Digit(No)

    print("Number of digit is : ",result)

if __name__ == "__main__":
    main()