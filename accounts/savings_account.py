from accounts.current_account import CurrentAccount

class SavingsAccount(CurrentAccount):
    def __init__(self, balance, firstname, lastname, account_number, interest_rate):
        super().__init__(balance, firstname, lastname, account_number)
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate

    # def set_interest_rate(self, interest_rate):
    #     self.interest_rate = interest_rate

    def calculate_interest(self, balance, interest_rate):
        self.interest_rate = (balance + (balance * (interest_rate/100)))
        return self.interest_rate
