from bank_account import *

Carl = bankAccnt(1200, "Carl")
Sally = bankAccnt(1500, "Sally")

Carl.getBalance()
Sally.getBalance()


Carl.deposit(500)
Sally.deposit(500)

Carl.withdraw(1000000)
Carl.withdraw(10)

Carl.transfer(100000, Sally)
Carl.transfer(100, Sally)

Jim = InterestRewardsAcct(1000,"Jim")

Jim.getBalance()
Jim.deposit(100)

Jim.transfer(100,Carl)

Blaze = SavinsAcc(1000, "blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(10000, Sally)