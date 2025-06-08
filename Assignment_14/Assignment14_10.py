class Employee:
    def __init__(self, name, department, salary):
        self.name = name               
        self._department = department  
        self.__salary = salary         

    def show(self):
        print("Name:", self.name)
        print("Department:", self._department)
        print("Salary:", self.__salary)

def main():
    obj = Employee("David", "IT", 60000)
    obj.show()
    print("Name (public):", obj.name)
    print("Department (protected):", obj._department)
    print("Salary (private):", obj._Employee__salary)

if __name__ == "__main__":
    main()
