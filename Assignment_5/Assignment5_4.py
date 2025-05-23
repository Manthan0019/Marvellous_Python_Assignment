def Largest(NO):
    a = NO[0]
    b = NO[1]
    c = NO[2]

    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

    


def main():
    data = []
    print("Enter tree numbers : ")
    for i in range(3):
        no = int(input())
        data.append(no)

    ret = Largest(data)
    
    print("Largest : ",ret)


if __name__ == "__main__":
    main()