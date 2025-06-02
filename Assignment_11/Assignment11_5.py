def countZero(No):
    if No == 0:
        return 1  
    digit = No % 10
    if No < 10:
        return 1 if digit == 0 else 0
    if digit == 0:
        return 1 + countZero(No // 10)
    else:
        return countZero(No // 10)

        
    

def main():
    print("Enter a number:")
    num = int(input())
    print("Number of zeros:", countZero(num))

if __name__ == "__main__":
    main()
