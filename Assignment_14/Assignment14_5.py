class BankAccount:

    def __init__(self,A,B):
        self.Account_number = A
        self.Name = B
        self.Balance = 0

    def deposit(self):
        print("Enter amount to deposite : ")
        amt = int(input())

        self.Balance = self.Balance + amt
        print("Deposited : ",self.Balance)

    def withdraw(self):
        print("enter amount to withdraw : ")
        amt = int(input())

        self.Balance = self.Balance - amt
        print("Withdrawn : ",self.Balance)
       
    def Display(self):
        print("Available balance : ",self.Balance)

def main():

    obj1 = BankAccount(12345678,"Manthan")
    obj1.deposit()
    obj1.withdraw()
    obj1.Display()

if __name__ == "__main__":
    main()
