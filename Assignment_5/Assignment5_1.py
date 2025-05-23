
def Add(No1 , No2):
    return  No1 + No2
    

def Sub(No1 , No2):
    return No1 - No2
    

def Mult(No1 , No2):
    if((No1 == 0) or (No2 == 0)):
        print("Multiplication can not be done with zero, Enter valid numbers.")
        return 
    else:
        return No1 * No2

def Divide(No1 , No2):
    if(No2 == 0):
        print("Division is not possible with 0")
        return
    else:
        return No1 / No2

def main():
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter a secon number : ")
    Value2 = int(input())

    print("Sum : ",Add(Value1,Value2))
    print("Diffrence : ",Sub(Value1,Value2))
    print("Product : ",Mult(Value1,Value2))
    print("Division : ",Divide(Value1,Value2))

if __name__ == "__main__":
    main()