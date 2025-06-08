class Person:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
    
class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.Subject = subject
        self.Salary = salary

    def Display(self):
        print("Name of teacher : ",self.Name)
        print("Age of teacher : ",self.Age)
        print ("Subject : ",self.Subject)
        print("Salary : ",self.Salary)

def main():

    obj2 = Teacher("Manthan",19,"Maths",20000)

    obj2.Display()

if __name__ == "__main__":
    main() 