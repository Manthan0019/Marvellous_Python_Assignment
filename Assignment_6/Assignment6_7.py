def Largest(NO,length):
    max = NO[0]
    for i in range(length):
        if(NO[i] > max):
            max = NO[i]
    return max
        

def main():
    Data = []

    print("Enter no.of elements to store : ")
    size = int(input())

    print("Enter values : ")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    ret = Largest(Data,size)
    
    print("Largest number from lis is : ",ret)


if __name__ == "__main__":
    main()