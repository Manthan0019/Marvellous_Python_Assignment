def Fharenhite(NO):
    fahrenhite = (NO * 9/5) + 32
    return fahrenhite
    


def main():
    
    print("Enter a temperature in celcious : ")
    
    no = float(input())
        

    ret = Fharenhite(no)
    
    print("Temperature in farenhite is :",ret)


if __name__ == "__main__":
    main()