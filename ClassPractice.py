# class and object

class BankAccount:
    def __init__(self,account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    
    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: {self.balance}")

# Create an instance of BankAccount
account1 = BankAccount("123456789", "Alice", 1000)
# Display account information
account1.display_info()
# Deposit money
account1.deposit(500)
# Withdraw money
account1.withdraw(200)
# Display account information again
account1.display_info()