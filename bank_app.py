from accounts.current_account import CurrentAccount
from accounts.savings_account import SavingsAccount

malvina_current_account = CurrentAccount(850, "Malvina", "Kalbarczyk", 12345678)

malvina_c_account_number = malvina_current_account.get_account_number()
print(malvina_c_account_number)

malvina_current_account.deposit(150)
print(malvina_current_account.get_balance())

malvina_savings_account = SavingsAccount(3000, "Malvina", "Kalbarczyk", 24681357, 3)
malvina_s_account_number = malvina_savings_account.get_account_number()
print(malvina_s_account_number)

malvina_balance = malvina_savings_account.get_balance()
print(malvina_balance)

malvina_interest = malvina_savings_account.calculate_interest(3000, 3)
print(malvina_interest)