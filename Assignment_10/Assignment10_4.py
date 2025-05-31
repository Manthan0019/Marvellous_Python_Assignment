from functools import reduce

ChkNum = lambda X : (X % 2 == 0)
Square = lambda X : X **2
Sum = lambda X,Y : X + Y


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

    MData = list(map(Square,FData))
    print("map output : ",MData)

    RData = reduce(Sum,MData)
    print("Reduce output : ",RData)

if __name__ == "__main__":
    main()