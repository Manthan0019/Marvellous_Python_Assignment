def eligiblity(no):
    if(no >= 18):
        return True
    else:
        return False
    


def main():
    print("Enter your age : ")
    Value = int(input())

    ret = eligiblity(Value)

    if(ret == True):
        print("You are eligible to vote")
    else:
        print("Not eligible")



if __name__ == "__main__":
    main()