# Constants
MAX_WITHDRAW_FACTOR = 0.1
PENALTY_FEE = 5

class BankAccount:
    def __init__(self, acc_number, balance, name):
        self.acc_number = acc_number
        self.balance = balance
        self.name = name
        self.total_withdrawn = 0
        self.total_deposited = 0
        self.penalty_fees = 0
    
    def __str__(self):
        return f'\t{self.acc_number}\t\t{self.name}\t\t${self.balance}\t\t\t${self.total_withdrawn}\t\t\t${self.total_deposited}\t\t\t${self.penalty_fees}'

    def deposit(self, amount):
        self.balance += amount
        self.total_deposited += amount
        print(f'{self.name} deposited ${amount}.')
    
    def withdraw(self, amount, req_type='request'):

        self.balance -= amount
        self.total_withdrawn += amount
        
        if req_type == 'penalize':
            print(f'A penalty fee of ${PENALTY_FEE} was incurred on {self.name}\'s account.')
        elif req_type == 'request':
            print(f'{self.name} withdrew ${amount}.')
        

    def penalize(self):
        self.penalty_fees += PENALTY_FEE
        BankAccount.withdraw(self, PENALTY_FEE, 'penalize')