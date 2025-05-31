import threading
def SumEvenFactor(NO):
    Sum = 0
    for i in range(1,NO+1):
        if(NO % i == 0 and i % 2 == 0):
            Sum = Sum + i
    print(" Sum of Even factors of number is : ",Sum)

def SumOddFactor(No):
    Sum = 0
    for i in range(1,No+1):
        if(No % i == 0 and i % 2 != 0):
            Sum = Sum + i
    print(" Sum of odd factors of number is : ",Sum)



def main():
    print("Enter a number : ")
    Value = int(input())

    evenfactor = threading.Thread(target=SumEvenFactor,args=(Value,))
    oddfactor = threading.Thread(target=SumOddFactor,args =(Value,))

    evenfactor.start()
    oddfactor.start()


if __name__ == "__main__":
    main()