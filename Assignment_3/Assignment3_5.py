from MarvellousNum import ChkPrime

def ListPrime(Data):
    SumPrime = 0
    primlist = []

    for i in (Data):
        if(ChkPrime(i)):
            primlist.append(i)
            SumPrime = SumPrime + i
    print("list of prime numbers is : ",primlist)
    return SumPrime

    

def main():
    Arr = []

    print("Enter the number of element : ")
    size = int(input())

    print("Enter the elements : ")
    for i in range(size):
        no = int(input())
        Arr.append(no)

    Ret = ListPrime(Arr)

    print("Addition of prime numbers : ",Ret)

if __name__ == "__main__":
    main()


