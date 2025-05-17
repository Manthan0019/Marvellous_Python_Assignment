def AddFact(Value):
    fact = 0
    for i in range(1,Value):
        if(Value % i == 0):
            fact = fact + i
    return fact


def main():
    print("Enter a number : ")
    No = int(input())

    Ans = AddFact(No)

    print("Factorial is :",Ans)

if __name__ == "__main__":
    main()