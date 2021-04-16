from bank_account import BankAccount, MAX_WITHDRAW_FACTOR, PENALTY_FEE

# Moderated bank accounts that inherit from BankAccount
class ModeratedAccount(BankAccount):
    def __init__(self, acc_number, balance, name, primary_account):
        super().__init__(acc_number, balance, name)
        self.calcMaxWithdraw()
        self.primary_account = primary_account
    
    def calcMaxWithdraw(self):
        self.max_withdraw = MAX_WITHDRAW_FACTOR * self.balance

    def deposit(self, amount):
        super().deposit(amount)
        self.calcMaxWithdraw()

    def withdraw(self, amount, req_type='request'): # If only an amount is passed to withdraw(), req_type defaults to 'request'
        if req_type == 'penalize':
            super().withdraw(amount - PENALTY_FEE)
            return
        
        if amount > self.max_withdraw:
            self.penalize(amount)
            return
        
        super().withdraw(amount)
        self.primary_account.moderatorTransfer(amount, self)
        self.calcMaxWithdraw()

    def penalize(self, amount):
        print(f'*** {self.name} attempted to withdraw ${amount}, which is more than the maximum allowed amount. ${PENALTY_FEE} will be deducted from their withdrawal request and a ${PENALTY_FEE} penalty fee will be applied to {self.primary_account.name}. ***\n')
        
        self.penalty_fees += PENALTY_FEE
        self.withdraw(amount, 'penalize')
        self.calcMaxWithdraw()
        self.primary_account.penalize()