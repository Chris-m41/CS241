class BalanceError(Exception):
    def __init__(self, message):
        super().__init__(message)

class OutOfChecksError(Exception):
    def __init__(self, message):
        super().__init__(message)

class CheckingAccount:
    def __init__(self, starting_balance, num_checks):
        if starting_balance < 0:
            raise BalanceError("Starting balance cannot be negative.")

        self.balance = starting_balance
        self.check_count = num_checks

    def write_check(self, amount):
        if self.balance - amount < 0:
            raise BalanceError("Balance cannot be negative")
        if self.check_count <= 0:
            raise OutOfChecksError("Insufficient number of checks")
        self.balance -= amount
        self.check_count -= 1

    def display(self):
        print("Checks: {}, Balance: ${:.2f}".format(self.check_count, self.balance))

    def apply_for_credit(self, amount):
        pass

def display_menu():
        print()
        print("Commands:")
        print("  quit - Quit")
        print("  new - Create new account")
        print("  display - Display account information")
        print("  deposit - Desposit money")
        print("  check - Write a check")

def get_more_checks(account):
        more_checks = input("Would you like to buy more checks (yes/no)? ")
        if more_checks == "yes":
            account.balance -= 5
            account.check_count += 25

def main():
    acc = None
    command = ""


    while command != "quit":
        display_menu()
        command = input("Enter a command: ")
        if command == "new":
            try:
                balance = float(input("Starting balance: "))
                num_checks = int(input("Numbers of checks: "))
                acc = CheckingAccount(balance, num_checks)
            except BalanceError as ex:
                print("Error: {}".format(str(ex)))
        elif command == "display":
            acc.display()
        elif command == "deposit":
            amount = float(input("Amount: "))
            acc.deposit(amount)
        elif command == "check":
            try:
                amount = float(input("Amount: "))
                acc.write_check(amount)
            except BalanceError as ex:
                print("Error: {}".format(str(ex)))
            except OutOfChecksError as ex:
                print("Error: {}".format(str(ex)))
                get_more_checks(acc)
        elif command == "credit":
            amount = float(input("Amount: "))
            acc.apply_for_credit(amount)

if __name__ == "__main__":
    main()

