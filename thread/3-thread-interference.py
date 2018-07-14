import threading


class BankAccount:
  def __init__(self):
    self.bal = 0

  def deposit(self, amt):
    balance = self.bal
    self.bal = balance + amt

  def withdraw(self, amt):
    balance = self.bal
    self.bal = balance - amt

b = BankAccount()

t1 = threading.Thread(target=b.deposit, args=(amt,))
t2 = threading.Thread(target=b.withdraw, args=(amt,))

t1.start()
t2.start()
