from functools import reduce

def ChkPrime(No):
    if(No <= 1):
        return False
    for i in range(2,No):
        if(No % i == 0):
            return False
    return True

MultNum = lambda No:(No * 2)

MaxNum = lambda A , B: (A if A > B else B )



def main():
    Data = []

    print("Enter number of elements that you want to store : ")
    size = int(input())

    print("Enter the elements : ")
    for i in range(size):
        element = int(input())
        Data.append(element)

    FData = list(filter(ChkPrime,Data))
    print("Filter Data : ",FData)

    MData = list(map(MultNum,FData))
    print("map output : ",MData)

    RData = reduce(MaxNum,MData)
    print("Reduce output : ",RData)


if __name__ == "__main__":
    main()