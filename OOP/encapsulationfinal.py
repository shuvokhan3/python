class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")


    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

# Example usage
account = BankAccount("123456789", 1000)        
account.deposit(500)  # Deposited: 500. New balance: 1500
account.withdraw(200)  # Withdrew: 200. New balance: 130
print(f"Account Number: {account.get_account_number()}")  # Account Number: 123456789
print(f"Current Balance: {account.get_balance()}")  # Current Balance: 130

