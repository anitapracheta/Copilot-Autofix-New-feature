from bank_account import BankAccount

def main():
    account1 = BankAccount("123456", "John Doe", 1000)
    account2 = BankAccount("654321", "Jane Doe", 500)

    account1.deposit(500)
    account1.withdraw(200)
    account1.transfer(account2, 300)

    print(f"Account 1 balance: {account1.get_balance()}")
    print(f"Account 2 balance: {account2.get_balance()}")

if __name__ == "__main__":
    main()
