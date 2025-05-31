import threading
def Even():
    Data = []
    for i in range(11):
        if(i % 2 == 0):
            Data.append(i)
    print("Evene numbers are : ",Data)

def Odd():
    Data = []
    for i in range(11):
        if(i % 2 != 0):
            Data.append(i)
    print("Odd numbers are : ",Data)



def main():
    
    EvenT = threading.Thread(target=Even)
    OddT = threading.Thread(target=Odd)

    EvenT.start()
    OddT.start()


if __name__ == "__main__":
    main()