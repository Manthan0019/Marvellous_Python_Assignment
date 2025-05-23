def ChkPrime(Value):
    if (Value <= 1):
        return False
    for i in range(2,Value):
        if (Value % i == 0):
            return False
    return True


def main():
    print("Enter a number : ")
    No = int(input())

    Ans = ChkPrime(No)

    if(Ans == True):
        print("The number is prime")
    else:
        print("The number is not prime")

    

if __name__ == "__main__":
    main()