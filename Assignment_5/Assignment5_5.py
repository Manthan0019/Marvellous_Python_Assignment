def EvenOdd(NO):
    if(NO % 2 == 0):
        return True
    else:
        return False
    


def main():
    
    print("Enter a number : ")
    
    no = int(input())
        

    ret = EvenOdd(no)
    
    if(ret == True):
        print(no,"Is Even")
    else:
        print(no,"is Odd")


if __name__ == "__main__":
    main()