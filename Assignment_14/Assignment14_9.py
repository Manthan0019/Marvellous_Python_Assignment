class Product:
    def __init__(self,name,price):
        self.Name = name
        self.Price = price
    
    def __eq__(self, other):
        return self.Price == other.Price

def main():
    product1 = Product("Mobile",30000)
    product2 = Product("Laptop",50000)

    if product1 == product2:
        print("Both products have the same price.")
    else:
        print("Products have different prices.")

if __name__ == "__main__":
    main()