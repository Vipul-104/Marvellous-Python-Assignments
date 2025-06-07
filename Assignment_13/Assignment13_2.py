class BankAccount:
    ROI = 10.5
    def __init__(self):
        print("Enter the name of Account Holder :")
        self.Name = input()
        self.Amount = 0

    def Diposite(self,):
        print("Enter the Amount to be diposite:")
        amt = int(input())
        self.Amount = self.Amount + amt

    def Withdraw(self):
        print("Enter the amount which shoulf be withdraw :")
        WAmt = int(input())
        self.Amount = self.Amount - WAmt

    def CalculateInterest(self):
        self.Interest = (self.Amount * BankAccount.ROI * 10)/100
    
    def Display(self):
        print("Name of the Account Holder :",self.Name)
        print("Account Balance",self.Amount)
        print("The interest is:",self.Interest)
 
    
def main():
    obj1 = BankAccount()
    obj1.Diposite()
    obj1.Withdraw()
    obj1.CalculateInterest()
    obj1.Display()

    print("_______________________")
    obj2 = BankAccount()
    obj2.Diposite()
    obj2.Withdraw()
    obj2.CalculateInterest()
    obj2.Display()

if __name__ ==  "__main__":
    main()