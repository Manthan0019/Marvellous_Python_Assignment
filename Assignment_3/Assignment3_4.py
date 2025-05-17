def NumFrequency(Data,Size,Num):

    Frequency = 0

    for i in range(Size):
        if(Data[i] == Num):
            Frequency = Frequency + 1
    return Frequency

def main():
    Arr = []

    print("Enter number of elements : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        Arr.append(no)
    
    print("Element to search : ")
    element = int(input())
    
    Ans = NumFrequency(Arr,size,element)

    print("Frequency of number is : ",Ans)


if __name__ == "__main__":
    main()