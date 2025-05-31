from functools import reduce

prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, n))
mult = lambda X : X *2
MaxNum = lambda A , B: (A if A > B else B )

def main():
    Data = []
    print("Enter number of elements that you want to store : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    FData = list(filter(prime,Data))
    print("Filter Data : ",FData)

    MData = list(map(mult,FData))
    print("map output : ",MData)

    RData = reduce(MaxNum,MData)
    print("Reduce output : ",RData)

if __name__ == "__main__":
    main()