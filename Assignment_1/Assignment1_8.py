def Display(Value):
    No = Value

    for i in range(No):
        print("*")

def main():
    print("Enter a Value : ")
    Num = int(input())

    Display(Num)

if __name__ == "__main__":
    main()