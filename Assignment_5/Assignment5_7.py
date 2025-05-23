def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)
    


def main(): 
    print("Enter a length : ")
    no1 = int(input())
    print("Enter a width : ")
    no2 = int(input())

    print("Area : ",rectangle_area(no1,no2))
    print("Perimeter : ",rectangle_perimeter(no1,no2))

        


if __name__ == "__main__":
    main()