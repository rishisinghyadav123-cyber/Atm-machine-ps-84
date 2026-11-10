import os

FILE_NAME = "atm.txt"
DEFAULT_PIN = "1234"


# -----------------------------
# File Handling Functions
# -----------------------------

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            file.write("10000\n")


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

            balance = float(lines[0].strip())

            transactions = []

            if len(lines) > 1:
                transactions = [line.strip() for line in lines[1:]]

            return balance, transactions

    except Exception:
        return 10000, []


def save_data(balance, transactions):
    try:
        with open(FILE_NAME, "w") as file:
            file.write(f"{balance}\n")

            for transaction in transactions:
                file.write(transaction + "\n")

    except Exception as e:
        print("File Error:", e)


# -----------------------------
# ATM Functions
# -----------------------------

def check_balance(balance):
    print(f"\nCurrent Balance: {balance}")


def deposit(balance, transactions):
    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Invalid amount.")
            return balance

        balance += amount

        transactions.append(
            f"Deposit {int(amount)} | Balance: {int(balance)}")

        save_data(balance, transactions)

        print(f"Deposit successful. New Balance: {int(balance)}")

        return balance

    except ValueError:
        print("Invalid amount. Please enter numbers only.")
        return balance


def withdraw(balance, transactions):
    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount.")
            return balance

        if amount > balance:
            print("Insufficient balance.")
            return balance

        balance -= amount

        transactions.append(
            f"Withdraw {int(amount)} | Balance: {int(balance)}")

        save_data(balance, transactions)

        print(f"Withdrawal successful. New Balance: {int(balance)}")

        return balance

    except ValueError:
        print("Invalid amount. Please enter numbers only.")
        return balance


def mini_statement(transactions):
    print("\n----- MINI STATEMENT -----")

    if len(transactions) == 0:
        print("No transactions available.")
        return

    for transaction in transactions[-5:]:
        print(transaction)


# -----------------------------
# Login Function
# -----------------------------

def verify_pin():
    attempts = 3

    while attempts > 0:

        pin = input("Enter PIN: ")

        if pin == DEFAULT_PIN:
            print("Login successful")
            return True

        attempts -= 1

        if attempts > 0:
            print(f"Invalid PIN. Attempts left: {attempts}")

    print("Account locked. Exiting...")
    return False


# -----------------------------
# Main Program
# -----------------------------

def main():

    initialize_file()

    if not verify_pin():
        return

    balance, transactions = load_data()

    while True:

        print("\n====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Mini Statement")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit(balance, transactions)

        elif choice == "3":
            balance = withdraw(balance, transactions)

        elif choice == "4":
            mini_statement(transactions)

        elif choice == "5":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    main()