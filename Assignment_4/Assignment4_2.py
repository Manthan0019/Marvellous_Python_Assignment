mult = lambda X,Y :  (X * Y)

def main():
    print("Enter First number : ")
    No1 = int(input())
    print("Enter second number : ")
    No2 = int(input())

    if((No1 == 0) | (No2 == 0)):
        return
    ret = mult(No1,No2)

    print("Multiplication is : ",ret)

if __name__ == "__main__":
    main()