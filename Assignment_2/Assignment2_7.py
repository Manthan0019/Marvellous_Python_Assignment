def Display(Value):
    for i in range(1,Value+1):
        for j in range(1,Value+1):
            print(j ,end=" ")
        print()

def main():
    print("Enter a number : ")
    No = int(input())

    Display(No)


if __name__ == "__main__":
    main()