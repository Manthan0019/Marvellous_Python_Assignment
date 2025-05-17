def ChkPrime(Value):
    if(Value <= 1):
        return False
    for i in range(2,Value):
        if(Value % i == 0):
            return False
    return True

def main():
    print("Enter a number : ")
    No = int(input())

    Result = ChkPrime(No)

    if(Result == True):
        print("The number is prime number")
    else:
        print("Number is not prime number")

if __name__ == "__main__":
    main()
