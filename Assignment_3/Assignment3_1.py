def Addlist(Data):
    sum = 0
    for i in(Data):
        sum = sum + i
    return sum

def main():
    Arr = []

    print("Enter number of elements : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        Arr.append(no)
    
    Ans = Addlist(Arr)

    print("Addition of list is : ",Ans)


if __name__ == "__main__":
    main()