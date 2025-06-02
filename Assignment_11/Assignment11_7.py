i = 1
j = 1
def Display():
    global i,j
    if i <= 4:
        if j <= 4:
            if i >= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")  
            j = j + 1
            Display()  
        else:
            print()   
            j = 1    
            i = i + 1
            Display()  
        


def main():
    Display()

if __name__ == "__main__":
    main()