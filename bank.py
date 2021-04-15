# Temporary code to clear console output
import os
os.system('clear')

# Display current time when account states are printed
from datetime import datetime

class BankAccount:
    def __init__(self, acc_number, balance, name):
        self.acc_number = acc_number
        self.balance = balance
        self.name = name

    def __str__(self):
        return '\tAccount ID: %s' % self.acc_number + '\tAccount Holder: %s' % self.name + '\tAccount Balance: $%s' % self.balance

    def deposit(self, amount):
        self.balance += amount
        print(self.name + ' deposited $%d' % amount)
    
    def withdraw(self, amount):
        self.balance -= amount
        print(self.name + ' withdrew $%d' % amount)

# Moderated bank accounts that inherit from BankAccount
class ModeratedAccount(BankAccount):
    def __init__(self, acc_number, balance, name, primary_account):
        super().__init__(acc_number, balance, name)
        self.primary_account = primary_account

# Get current date and time
# Code adapted from https://www.programiz.com/python-programming/datetime/current-datetime
def currentTime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    return dt_string

# Print the states of all accounts
def printAccountStates(account_list):
    print('Account States as of ' + currentTime())
    for a in account_list:
        print(a)

# Initialize bank accounts
scrooge = BankAccount(100001, 1000000, 'Scrooge McDuck')
huey = ModeratedAccount(700007, 150, 'Huey Duck', scrooge)
dewy = BankAccount(800008, 350, 'Dewey Duck')
louie = BankAccount(900009, 25, 'Louie Duck')

# Store accounts in a list to easily print all states
account_list = [scrooge, huey, dewy, louie]


printAccountStates(account_list)




