import multiprocessing

def Square(No):
    result = []
    product = 0
    for i in (No):
        product = i * i
        result.append(product)
    print(result)


def main():
    Data = []
    print("Enter number of elements that you want to store : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)


    T1 = multiprocessing.Process(target=Square,args=(Data,))

    T1.start()
    T1.join()
    
if __name__ == "__main__":
    main()