import threading

def CountSmall(st):
    print("The id of current thread is : ",threading.get_ident())
    count = 0
    for ch in st:
        if(ch >= 'a' and ch <='z'):
            count = count + 1
    print("Count of small is : ",count)

def CountCapital(st):
    print("The id of current thread is : ",threading.get_ident())
    count = 0
    for ch in st:
        if(ch >= 'A' and ch <='Z'):
            count = count + 1
    print("Count of Capital is : ",count)

def CountDigit(st):
    print("The id of current thread is : ",threading.get_ident())
    count = 0
    for ch in st:
        if(ch >= '0' and ch <= '9'):
            count = count + 1
    print("Count od digit is : ",count)    


def main():
    print("Enter a string z : ")
    data = input()

    small = threading.Thread(target=CountSmall,args=(data,))
    capital = threading.Thread(target=CountCapital,args=(data,))
    digit = threading.Thread(target=CountDigit,args=(data,))

    small.start()
    capital.start()
    digit.start()

    small.join()
    capital.join()
    digit.join()
    

if __name__ == "__main__":
    main()