class BankAccount:
    ROI = 10.5

    def __init__(self,A):
        self.Name = A
        self.Amount = 0

    def Deposite(self):
        print("Enter amount to deposite : ")
        amt = int(input())

        self.Amount = amt
        print("Amount after deposite : ",self.Amount)

    def Withdraw(self):
        print("Enter amount that you want to withdraw : ")
        amt = int(input())

        self.Amount = self.Amount - amt
        print("Amount after withdraw : ",self.Amount)

    def Calculateinteraset(self):
        BankAccount.ROI = (BankAccount.ROI * self.Amount)/100
        print("Interest on balance is : ",BankAccount.ROI)

    def Display(self):
        print("---- Account Details ----")
        print("Account Holder Name:", self.Name)
        print("Current Balance:", self.Amount)
        print("Interest :", BankAccount.ROI)
        print("--------------------------")

def main():
    obj1 = BankAccount("Manthan")
    obj1.Deposite()
    obj1.Withdraw()
    obj1.Calculateinteraset()
    obj1.Display()

if __name__ == "__main__":
    main()