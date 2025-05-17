def Factorial(Value):
    fact = 1
    for i in range(1,Value+1):
        fact = fact * i
    return fact


def main():
    print("Enter a number : ")
    No = int(input())

    Ans = Factorial(No)

    print("Factorial is :",Ans)

if __name__ == "__main__":
    main()