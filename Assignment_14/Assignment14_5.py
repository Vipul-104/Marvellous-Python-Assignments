class BankAccount:
    def __init__(self):
        print("Enter The Acc no:")
        self.Account_number = int(input())

        print("Enter Your Name:")
        self.name = input()

        self.Balance = 0

    def Deposite(self):
        print("Enter the Diposited Amount:")
        amt = int(input())
        self.Balance = self.Balance + amt

    def Withdraw(self):
        print("Enter the Withdrawal amount:")
        Wamt = int(input())
        if(self.Balance >= Wamt):
            self.Balance = self.Balance - Wamt
        else:
            print("Your Accoubnt Has Unsufficient Balance to Withdraw")


    def Display(self):
        print(self.Account_number)
        print(self.name)
        print("The Balance Is:",self.Balance )


def main():
    obj1 = BankAccount()
    obj1.Deposite()
    obj1.Withdraw()
    obj1.Display()

    print("_________________________")

    obj2 = BankAccount()
    obj2.Deposite()
    obj2.Withdraw()
    obj2.Display()

if __name__ == "__main__":
    main()