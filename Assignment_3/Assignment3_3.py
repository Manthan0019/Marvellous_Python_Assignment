def Minlist(Data,Size):

    Minimum = Data[0]

    for i in range(Size):
        if(Data[i] < Minimum):
            Minimum = Data[i]
    return Minimum

def main():
    Arr = []

    print("Enter number of elements : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        Arr.append(no)
    
    Ans = Minlist(Arr,size)

    print("Minimum from list is : ",Ans)


if __name__ == "__main__":
    main()