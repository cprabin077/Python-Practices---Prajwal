# 3.	Create a Bank Account class with methods for deposit, withdraw, and check balance.

# Create Class
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return "Deposited: " + str(amount)

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return "Withdrawn: " + str(amount)

    
    def check_balance(self):
        return self.balance
    
    def display_details(self):
        print("Bank Account Details:")
        print("----------------------")
        print("Current Balance :", self.balance)

# Create object
account1 = Account(10000)

# Display details
account1.display_details()

# Deposit
print(account1.deposit(1000))
print("Balance:", account1.check_balance())

# Withdraw
print(account1.withdraw(8000))
print("Balance:", account1.check_balance())

# Withdraw
print(account1.withdraw(5000))
print("Balance:", account1.check_balance())




    
