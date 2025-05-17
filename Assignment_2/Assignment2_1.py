import Arithmatic

def main():
    print("Enter first a number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    print("Select the opertation you want to perform : ")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice = int(input())

    if (choice == 1) :
        Ans = Arithmatic.Add(Value1, Value2)
        print("Addition is : ",Ans)
    elif(choice == 2):
        Ans = Arithmatic.Sub(Value1, Value2)
        print("Substraction is : ",Ans)
    elif(choice == 3):
        Ans = Arithmatic.Mult(Value1 , Value2)
        print("Multiplication is : ",Ans)
    else:
        Ans = Arithmatic.Divide(Value1,Value2)
        print("Division is : ",Ans)

if __name__ == "__main__":
    main()