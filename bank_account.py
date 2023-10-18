
#this class is to set up the withdrawal function to prevent withdrawals over the amount in account
class BalanceException(Exception):
    pass

#this class is the bank account
class bankAccnt:
    def __init__(self,initial_amount, accountName):
        self.balance=initial_amount
        self.name = accountName
        print(f"\n Account '{self.name}' created.\nBalance = ${self.balance:.2f}")

#This function is used to get the a balance
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance=${self.balance:.2f}")
#This function is used to deposit
    def deposit(self, amount):
        self.balance=self.balance+ amount
        print("\nDeposit Complete.")
        self.getBalance()
#Checking if viable transaction
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )


    def withdraw(self,amount):
        #the try is there to catch the exception so that the withdrawal wont be more than the amount
        try:
            self.viableTransaction(amount)
            self.balance = self.balance-amount
            print("\nWithdrawal complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdrawal is interupted: {error}')

#transferring function
    def transfer(self,amount,account):
        try:
            print("\n **********\n\nBeginning Transfer....")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!\n\n**********")
        except BalanceException as error:
            print(f"\nTansfer interrupted.{error}")
#Creating a class for interest calculations
class InterestRewardsAcct(bankAccnt):
    def deposit(self, amount):
        self.balance=self.balance +(amount*1.05)
        print("\nDeposit complete.")
        self.getBalance()


class SavinsAcc(InterestRewardsAcct):
    def __int__(self, InitialAmount,acctName):
        super().__init__(InitialAmount,acctName)
        self.fee=5
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance = self.balance-(amount+self.fee)
            print("\nWithdrawal completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\n Withraw interrupted{error}")