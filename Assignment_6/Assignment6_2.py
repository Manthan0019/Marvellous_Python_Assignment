def Display():
    sum = 0
    for i in range(1,100+1):
        if(i % 2 == 0):
            sum = sum + i
    return sum
def main():
    ret = Display()
    print("Sum of even numbers between 1 to 100 is : ",ret)

if __name__ == "__main__":
    main()