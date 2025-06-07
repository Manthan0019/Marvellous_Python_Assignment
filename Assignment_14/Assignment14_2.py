class Rectangle:
    def __init__(self,A,B):
        self.length = A
        self.width = B


    def Area(self):
        RectArea = self.width * self.length
        print("Area of Rectangle is : ",RectArea)
    
    def Perimeter(self):
        RectPerimeter = (2 * (self.length + self.width))
        print("Perimeter of rectangle is : ",RectPerimeter)

def main():

    obj1 = Rectangle(50,30)
    obj1.Area()
    obj1.Perimeter()

if __name__ == "__main__":
    main()
