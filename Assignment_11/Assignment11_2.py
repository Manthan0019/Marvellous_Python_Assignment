i = 1  
fact = 1  

def Factorial(No):
    global i, fact
    if (i <= No):
        fact = fact * i
        i = i + 1
        Factorial(No)
    return fact

def main():
    print("Enter a number :")
    Value = int(input())

    Ret = Factorial(Value)
    print("Factorial : ",Ret)

if __name__ == "__main__":
    main()