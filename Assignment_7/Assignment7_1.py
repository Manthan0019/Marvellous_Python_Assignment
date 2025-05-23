square = lambda X : X ** 2
cube = lambda X : X ** 3

def main():
    print("Enter a number : ")
    no = int(input())

    print("Square is : ",square(no))
    print("Cube is : ",cube(no))

if __name__ == "__main__":
    main()
