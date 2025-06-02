def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

def main():
    print("Enter a number:")
    value = int(input())
    print("Enter a power that you want to find:")
    exponent = int(input())

    result = power(value, exponent)
    print("Power of the number:", result)

if __name__ == "__main__":
    main()
