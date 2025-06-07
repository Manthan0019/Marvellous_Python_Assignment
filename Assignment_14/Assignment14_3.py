class Book:
    def __init__(self,A):
        self.__price = A
       
    def Display(self):
        print(self.__price)

def main():

    obj1 = Book(500)
    obj1.Display()
    

if __name__ == "__main__":
    main()
