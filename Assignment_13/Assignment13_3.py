class Numbers:
    def __init__(self, value):
        self.Value = value

    def Factors(self):
        print(self.Value,"'s Factors are: ")
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum = sum + i
        print("Sum of the factors is : ",sum)
        return sum

    def ChkPrime(self):
        if self.Value <= 1:
            print(self.Value,"is not prime")
        for i in range(2, self.Value):
            if self.Value % i == 0:
                print(self.Value,"is not prime")
        print(self.Value,"is a prime")

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            print(self.Value,"is perfect")
        else:
            print(self.Value,"is not perfect")


def main():
    obj1 = Numbers(11)
    obj2 = Numbers(21)
    obj3 = Numbers(51)


    obj1.Factors()
    obj1.ChkPrime()
    obj1.ChkPerfect()
    

    obj2.Factors()
    obj2.ChkPrime()
    obj2.ChkPerfect()

    obj3.Factors()
    obj3.ChkPrime()
    obj3.ChkPerfect()

if __name__ == "__main__":
    main()
