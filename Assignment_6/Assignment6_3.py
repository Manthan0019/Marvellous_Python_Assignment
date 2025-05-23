def DisplayTable(no):
    table = []
    result = 0
    i = 1

    while(i <= 10):
        result = no * i
        table.append(result)
        i = i + 1
    return table

def main():
    print("Enter a number : ")
    num = int(input())

    ret = DisplayTable(num)
    print(ret)

if __name__ == "__main__":
    main()