def Maxlist(Data,Size):

    Maximum = Data[0]

    for i in range(Size):
        if(Data[i] > Maximum):
            Maximum = Data[i]
    return Maximum

def main():
    Arr = []

    print("Enter number of elements : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        Arr.append(no)
    
    Ans = Maxlist(Arr,size)

    print("Maximum from list is : ",Ans)


if __name__ == "__main__":
    main()