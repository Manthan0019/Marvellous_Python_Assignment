import multiprocessing

def Factorial(values):
    fact = 1
    for i in range(1,values+1):
        fact = fact * i
    return fact

def main():
    Data = []
    print("Enter number of elements that you want to store : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    P1 = multiprocessing.Pool()

    result = P1.map(Factorial,Data)

    P1.close()
    P1.join()

    print(result)
    
if __name__ == "__main__":
    main()