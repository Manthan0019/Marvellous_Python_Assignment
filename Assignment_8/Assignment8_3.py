import threading

def SumEven(numbers):
    Sum = 0
    for num in numbers:
        if num % 2 == 0:
            Sum = Sum + num
    print("Sum of Even numbers is:", Sum)

def SumOdd(numbers):
    Sum = 0
    for num in numbers:
        if num % 2 != 0:
            Sum = Sum + num
    print("Sum of Odd numbers is:", Sum)

def main():
    Data = []
    print("Enter number of elements that you want to store:")
    Size = int(input())

    print("Enter elements:")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    evenlist = threading.Thread(target=SumEven, args=(Data,))
    oddlist = threading.Thread(target=SumOdd, args=(Data,))

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()

if __name__ == "__main__":
    main()
