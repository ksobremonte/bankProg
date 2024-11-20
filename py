# Define the Account class
class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")

    def get_balance(self):
        return self.balance

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")


# Define the Bank class
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_deposit=0.0):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            account = Account(account_number, name, initial_deposit)
            self.accounts[account_number] = account
            print("Account created successfully.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)


# Example of user interaction
def main():
    bank = Bank()
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(acc_num, name, initial_deposit)

        elif choice == '2':
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                print(f"Current balance: {account.get_balance()}")
            else:
                print("Account not found.")

        elif choice == '5':
            print("Thank you for using the banking system.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
