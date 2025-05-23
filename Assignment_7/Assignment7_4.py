from functools import reduce

Product = lambda A,B : A * B


def main():
    data = []
    print("Enter a no.of elements : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("Even numbers : ",reduce(Product,data))
    

if __name__ == "__main__":
    main()
