class BookStore:
    NoOfBooks = 0

    def __init__(self,A,B):
        self.Name = A
        self.Author = B
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Diaplay(self):
        print(self.Name,"by",self.Author,"No.of books :",BookStore.NoOfBooks)

def main():
    obj1 = BookStore("Linux system programming","Robert Love")
    obj1.Diaplay()

    obj2 = BookStore("C Programming","Dennis Ritchie")
    obj2.Diaplay()

if __name__ == "__main__":
    main()