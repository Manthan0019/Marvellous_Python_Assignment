Evene = lambda No : (No % 2 == 0)


def main():
    data = []
    print("Enter a no.of elements : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("Even numbers : ",list(filter(Evene,data)))
    

if __name__ == "__main__":
    main()
