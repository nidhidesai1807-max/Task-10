class BankAccount:
    bank_name = "Simple Bank"

    def __init__(self, holder_name, account_number, balance=0.0):
        self.holder_name = holder_name
        self.account_number = account_number
        self.__balance = float(balance)

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.__balance += amount
        return f"Deposited {amount:.2f}. New balance: {self.__balance:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdraw amount must be positive."
        if amount > self.__balance:
            return "Insufficient balance."
        self.__balance -= amount
        return f"Withdrawn {amount:.2f}. New balance: {self.__balance:.2f}"

    def transfer(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            return "Transfer failed: invalid account."
        if amount <= 0:
            return "Transfer amount must be positive."
        if amount > self.__balance:
            return "Transfer failed: insufficient balance."

        self.__balance -= amount
        other_account._BankAccount__balance += amount
        return f"Transferred {amount:.2f} to {other_account.holder_name}. Balance: {self.__balance:.2f}"

    def account_info(self):
        return f"{self.bank_name} | {self.holder_name} | Acc: {self.account_number} | Balance: {self.__balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, holder_name, account_number, balance=0.0, min_balance=500.0):
        super().__init__(holder_name, account_number, balance)
        self.min_balance = float(min_balance)

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdraw amount must be positive."

        current_balance = self.get_balance()
        if current_balance - amount < self.min_balance:
            return f"Withdraw denied: Minimum balance {self.min_balance:.2f} must be maintained."

        return super().withdraw(amount)


class CurrentAccount(BankAccount):
    def __init__(self, holder_name, account_number, balance=0.0, overdraft_limit=2000.0):
        super().__init__(holder_name, account_number, balance)
        self.overdraft_limit = float(overdraft_limit)

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdraw amount must be positive."

        available = self.get_balance() + self.overdraft_limit
        if amount > available:
            return "Withdraw denied: Overdraft limit exceeded."

        self._BankAccount__balance -= amount
        return f"Withdrawn {amount:.2f}. New balance: {self.get_balance():.2f}"


def main():
    acc1 = SavingsAccount("Nidhi", "SB1001", 5000, min_balance=1000)
    acc2 = CurrentAccount("Rahul", "CA2001", 2000, overdraft_limit=3000)
    acc3 = BankAccount("Meera", "BA3001", 1000)

    accounts = [acc1, acc2, acc3]

    print("\n--- Initial Accounts ---")
    for acc in accounts:
        print(acc.account_info())

    print("\n--- Operations ---")
    print(acc1.deposit(1200))
    print(acc1.withdraw(4500))
    print(acc1.withdraw(3800))

    print(acc2.withdraw(4000))
    print(acc2.withdraw(2000))

    print(acc3.transfer(acc1, 500))
    print(acc3.transfer(acc2, 800))

    print("\n--- Final Accounts ---")
    for acc in accounts:
        print(acc.account_info())


if __name__ == "__main__":
    main()
