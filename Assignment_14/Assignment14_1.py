class Employee:
    def __init__(self,A,B,C):
        self.Name = A
        self.emp_id = B
        self.salary = C

    def display(self):
        print("Name:", self.Name, "ID:", self.emp_id, "Salary:", self.salary)

def main():

    obj1 = Employee("Sham",101,50000)
    obj1.display()

if __name__ == "__main__":
    main()
