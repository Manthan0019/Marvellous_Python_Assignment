palindrome = lambda s: s == s[::-1]

def main():
    print("Enter string : ")
    sample = input()

    ret = palindrome(sample)

    if(ret == True):
        print(sample,"is palindrome")
    else:
        print(sample,"is not palindrome")
    

if __name__ == "__main__":
    main()
