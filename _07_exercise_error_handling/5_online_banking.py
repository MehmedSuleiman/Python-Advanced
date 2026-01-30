class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

def send_money(amount, given_pin, account_pin, balance, age) :
    if amount > balance:
        raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
    if str(given_pin) != str(account_pin):
        raise PINCodeError("Invalid PIN code")
    if age < 18:
        raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

    balance -= amount
    print(f"Successfully sent {amount:.2f} money to a friend")
    print(f"There is {balance:.2f} money left in the bank account")
    return balance

def receive_money(amount):
    if amount < 0:
        raise MoneyIsNegativeError("The amount of money cannot be a negative number")
    half = amount / 2
    print(f"{half:.2f} money went straight into the bank account")
    return half


first_line = input().split(", ")
account_pin = first_line[0]
balance = float(first_line[1])
age = int(first_line[2])

while True:
    line = input()
    if line == "End":
        break
    parts = line.split("#")
    command = parts[0]

    if command == "Send Money":
        amount = float(parts[1])
        given_pin = parts[2]
        balance = send_money(amount, given_pin, account_pin, balance, age)
    elif command == "Receive Money":
        amount = float(parts[1])
        added = receive_money(amount)
        balance += added


