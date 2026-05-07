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
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")
    def get_balance(self):
        return self.__balance   
    
obj = BankAccount("123456789", 1000)
obj.deposit(500)  # Deposited: 500. New balance: 1500
obj.withdraw(200)  # Withdrew: 200. New balance: 130
print(obj.get_balance())  # 1300
# Attempting to access private attributes directly will result in an error
# print(obj.__balance)  # This will raise an AttributeError