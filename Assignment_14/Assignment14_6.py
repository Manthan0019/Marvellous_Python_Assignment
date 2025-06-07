class Arithmatic:

    def __init__(self,A,B):
        self.Value1 = A
        self.Value2 = B

    def add(self):
        print("Addition is : ",self.Value1 + self.Value2)

    def subtract(self):
        print("Subtraction is : ",self.Value1 - self.Value2)

    def multiply(self):
        print("Multiplication is : ",self.Value1 * self.Value2)

    def divide(self):
        if self.Value2 != 0:
            print("Division is :",self.Value1 / self.Value2)
        else:
            return "Cannot divide by zero"

def main():
    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    No2 = int(input())

    obj = Arithmatic(No1,No2)

    print("Please select the operation : ")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiply")
    print("4.Divide")
    choice = int(input())

    if (choice == 1):
        obj.add()
    elif(choice == 2):
        obj.subtract()
    elif(choice == 3):
        obj.multiply()
    else:
        obj.divide()

    

if __name__ == "__main__":
    main()
