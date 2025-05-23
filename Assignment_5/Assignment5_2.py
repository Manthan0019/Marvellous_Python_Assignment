def ChkVowel(ch):
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        print(ch,"is vowel")
    else:
        print(ch,"is not vowel")
    
def main():
    print("Enter character : ")
    Value = input()
    ChkVowel(Value)

if __name__ == "__main__":
    main()