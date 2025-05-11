def Add(Value1, Value2):
    result = Value1 + Value2
    return result

def main():
    print("Enter first number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    Ans = Add(no1 , no2)
    print("Addition is : ",Ans)



if __name__ == "__main__":
    main()
