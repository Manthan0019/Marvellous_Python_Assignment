i = 0
sum = 0

def SumNatural(No):
    global i,sum

    if(i <= No):
        sum = sum + i
        i = i + 1
        SumNatural(No)
    return sum

def main():
    print("Enter a number:")
    Value = int(input())

    Ret = SumNatural(Value)
    print("Sum of natural numbers:", Ret)

if __name__ == "__main__":
    main()
