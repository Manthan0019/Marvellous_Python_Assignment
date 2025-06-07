class Student:
    school_name = "international school"

    def __init__(self,A,B):
        self.Name = A
        self.Roll_No = B

       
    def Display(self):
        print("Name:", self.Name)
        print("Roll No:", self.Roll_No)
        print("School:", Student.school_name)

def main():

    obj1 = Student("Manthan",19)
    obj1.Display()
    Student.school_name = "National School"
    obj1.Display()
    

if __name__ == "__main__":
    main()
