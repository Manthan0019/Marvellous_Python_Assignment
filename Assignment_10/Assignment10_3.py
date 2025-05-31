from functools import reduce

ChkNum = lambda X : X >= 70 and X <= 90
Increase = lambda X : X + 10
product = lambda X,Y : X * Y


def main():
    Data = []
    print("Enter number of elements that you want to store : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    FData = list(filter(ChkNum,Data))
    print("Filter Data : ",FData)

    MData = list(map(Increase,FData))
    print("map output : ",MData)

    RData = reduce(product,MData)
    print("Reduce output : ",RData)

if __name__ == "__main__":
    main()