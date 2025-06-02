i = 1
def Display(No):
    global i 
    if(i <= No):
        print(i)
        i = i + 1
        Display(No)

def main():
    print("Enter a number :")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()