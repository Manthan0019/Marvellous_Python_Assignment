def Display():
    i = 0
    j = 0

    for i in range(4):
        for j in range(4):
            if(i >= j):
                print("*",end=" ")
        print()
        

def main():
    Display()

if __name__ == "__main__":
    main()