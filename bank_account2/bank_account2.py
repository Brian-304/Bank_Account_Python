#Class
class BankAccount:		
    def __init__(self, int_rate, balance):
    #Attributes
        self.int_rate = int_rate
        self.account_balance = 0
    #Methods
    def make_deposit(self, amount):
        self.account_balance += amount
        print("\n Amount Deposited:", amount)
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print("\n You Withdrew:", amount)
    def yield_interest(self):
        self.account_balance *= (self.int_rate + 1)
    def display_account_info(self):
        print("Net Available Balance:")
        return(self.account_balance)

brian = BankAccount(.01, 0)
monty = BankAccount(.01, 0)

#Call methods
monty.make_deposit(500)
monty.make_withdrawal(100)
monty.yield_interest()
brian.make_deposit(150)
brian.make_withdrawal(50)
brian.yield_interest()

print(brian.display_account_info())
print(monty.display_account_info())
