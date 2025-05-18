from functools import reduce

ChkNum = lambda No:(No >= 70) and (No <= 90)

AddNum = lambda No:(No + 10)

ProductNum = lambda A,B:(A * B)

def main():
    Data = []

    print("Enter number of elements that you want to store : ")
    size = int(input())

    print("Enter the elements : ")
    for i in range(size):
        element = int(input())
        Data.append(element)

    FData = list(filter(ChkNum,Data))
    print("Filter Data : ",FData)

    MData = list(map(AddNum,FData))
    print("map output : ",MData)

    RData = reduce(ProductNum,MData)
    print("Reduce output : ",RData)


if __name__ == "__main__":
    main()