from bank_account import BankAccount, MAX_WITHDRAW_FACTOR, PENALTY_FEE

# Moderator bank account that inherits from BankAccount
class ModeratorAccount(BankAccount):
    def __init__(self, acc_number, balance, name):
        super().__init__(acc_number, balance, name)
        self.moderated_accounts = []

    def deposit(self, amount):
        super().deposit(amount)

    def withdraw(self, amount, req_type='request'): # If only an amount is passed to withdraw(), req_type defaults to 'request'
        if req_type == 'penalize':
            super().withdraw(amount - PENALTY_FEE)
            return
        # elif req_type == 'moderator_transfer':
        #     pass
        
        super().withdraw(amount, req_type)

    def moderatorTransfer(self, amount, moderated_account_initiator):
        for a in self.moderated_accounts:
            if a != moderated_account_initiator:
                a.deposit(amount)
                self.withdraw(amount, 'moderator_transfer')
                # print(f'{self.name} deposited ${amount} into {a.name}\'s account.')

    # def penalize(self):
    #     super().penalize()