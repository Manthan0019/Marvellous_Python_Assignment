from functools import reduce

ChkEven = lambda No:(No % 2 == 0)

SqrNum = lambda No:(No ** 2)

SumNum = lambda A,B:(A + B)

def main():
    Data = []

    print("Enter number of elements that you want to store : ")
    size = int(input())

    print("Enter the elements : ")
    for i in range(size):
        element = int(input())
        Data.append(element)

    FData = list(filter(ChkEven,Data))
    print("Filter Data : ",FData)

    MData = list(map(SqrNum,FData))
    print("map output : ",MData)

    RData = reduce(SumNum,MData)
    print("Reduce output : ",RData)


if __name__ == "__main__":
    main()