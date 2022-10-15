
#Bank account class with attributes
class BankAccount:		
    def __init__(self, bank, int_rate, account_balance):
        self.bank = bank
        self.int_rate = int_rate
        self.account_balance = 0

#Bank account methods
    def make_deposit(self, amount):
        self.account_balance += amount
        
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        
    def yield_interest(self):
        self.account_balance *= (self.int_rate + 1)
        
    def display_account_info(self):
        print("\n Net Available Balance=", self.account_balance)

#Account 1
brian = BankAccount("First National Dojo", .01, 0)

#Account 2
monty = BankAccount("First National Dojo", .01, 0)


#Account 1 deposit and withdrawal
brian.make_deposit(100)
brian.make_deposit(100)
brian.make_deposit(250)
brian.make_withdrawal(200)
brian.yield_interest()


#Account 2 deposit and withdrawal
monty.make_deposit(300)
monty.make_deposit(400)
monty.make_withdrawal(10)
monty.make_withdrawal(20)
monty.make_withdrawal(30)
monty.make_withdrawal(40)
monty.yield_interest()


#Account 1 bank account using chaining
print(brian.bank, brian.account_balance, brian.int_rate), brian.display_account_info()

#Account 2 bank account using chaining
print(monty.bank, monty.account_balance, monty.int_rate), monty.display_account_info() 







