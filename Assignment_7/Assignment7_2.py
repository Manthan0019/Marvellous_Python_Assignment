Double = lambda X : X * 2


def main():
    data = []
    print("Enter a no.of elements : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("Doublled list : ",list(map(Double,data)))
    

if __name__ == "__main__":
    main()
