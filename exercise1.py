class BankAccount:
    ???

def main():
    my_account = BankAccount.create()
    your_account = BankAccount.create()
    print(my_account.balance) #--> 0
    print(BankAccount.total_funds()) #--> 0
    my_account.deposit(200)
    your_account.deposit(1000)
    print(my_account.balance) #--> 200
    print(your_account.balance) #--> 1000
    print(BankAccount.total_funds()) #--> 1200
    BankAccount.add_interest()
    print(my_account.balance) #--> 202.0
    print(your_account.balance) #--> 1010.0
    print(BankAccount.total_funds()) #--> 1212.0
    my_account.withdraw(50)
    print(my_account.balance) #--> 152.0
    print(BankAccount.total_funds()) #--> 1162.0

main()
