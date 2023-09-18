class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100

SA = SavingsAccount()

SA.balance = float(input("Enter initial balance: "))
SA.interestRate = float(input("Enter interest rate (%): "))

withdrawal_amount = float(input("Enter withdrawal amount: "))
SA.withdrawal(withdrawal_amount)

deposit_amount = float(input("Enter deposit amount: "))
SA.deposit(deposit_amount)

print("Updated balance:", SA.getBalance())

interest = SA.interestAmount()
print("Interest amount:", interest)