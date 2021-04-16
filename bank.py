from bank_account import BankAccount
from moderator_account import ModeratorAccount
from moderated_account import ModeratedAccount

# Temporary code to clear console output
import os
os.system('clear')

# Get current date and time
# Code adapted from https://www.programiz.com/python-programming/datetime/current-datetime
from datetime import datetime
def currentTime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    return dt_string

# Print the states of all accounts
def printAccountStates(account_list):
    print('\nAccount States as of ' + currentTime())
    print('\tAccount ID\tAccount Holder\t\tAccount Balance\t\tTotal Withdrawn\t\tTotal Deposited\t\tTotal Penalities')
    print('\t', end='')
    for i in range(0, 128):
        print('–', end='')
    print('')
    for a in account_list:
        print(a)
    print('\n')

# Initialize bank accounts
scrooge = ModeratorAccount(100001, 1000000, 'Scrooge McDuck')
huey = ModeratedAccount(700007, 150, 'Huey Duck', scrooge)
dewy = ModeratedAccount(800008, 350, 'Dewey Duck', scrooge)
louie = ModeratedAccount(900009, 25, 'Louie Duck', scrooge)

# Link moderated accounts to the primary account holder
scrooge.moderated_accounts = [huey, dewy, louie]


# Store accounts in a list to easily print all account states
account_list = [scrooge, huey, dewy, louie]

print('Welcome! Accessing your account information...\n')

printAccountStates(account_list)

louie.withdraw(2)
printAccountStates(account_list)

dewy.withdraw(20)
printAccountStates(account_list)

huey.withdraw(20)
printAccountStates(account_list)

louie.withdraw(10)
printAccountStates(account_list)

dewy.withdraw(20)
printAccountStates(account_list)

huey.withdraw(30)
printAccountStates(account_list)

louie.withdraw(40)
printAccountStates(account_list)