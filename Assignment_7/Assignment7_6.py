prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, n))

def main():
    data = []

    print("Enter no.of elements : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("Prime numbers are : ",list(filter(prime,data)))
    

if __name__ == "__main__":
    main()
