def Countlen(S):
    count = 0
    for i in S:
        count = count + 1
    
    return count
    
def main():
    print("Enter a name : ")
    Name = input()

    length = Countlen(Name)

    print("Length is : ",length)

if __name__ == "__main__":
    main()