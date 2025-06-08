class Vheical:
    def Start(self):
        print("Inside Vheical Start")

class Car(Vheical):
    def Start(self):
        print("Inside Derived Start")
        super().Start()

def main():
    obj1 = Vheical()
    obj2 = Car()

    obj1.Start()
    obj2.Start()

if __name__ == "__main__":
    main()