def Display(Value):
    for i in range(Value):
        for j in range(Value):
            if(j>=i):
                print("*" ,end=" ")
        print()

def main():
    print("Enter a number : ")
    No = int(input())

    Display(No)


if __name__ == "__main__":
    main()