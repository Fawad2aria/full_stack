class atm_account:
    def __init__(self):
        self.balance = 0
        self.transactions = []
    def check_blance(self):
        return self.balance


    def deposit(self,amount):
        self.transactions.append(f"user deposited ${amount}")
        self.balance = self.balance + amount
        print(f"Successful transaction! \nyou deposited ${amount} to your account.\nYour balance is ${self.balance}.\n")
        

    def check_withdrawal(self,amount):
        return self.balance >= amount

    def withdraw(self, amount):     

        if self.check_withdrawal(amount):
            self.transactions.append(f"user withdrew ${amount}")

            self.balance = self.balance - amount
            print(f"Successful Transaction!\nyou withdraw ${amount} from your ccount.\n")
            return amount
        else:
            self.transactions.append(f"Unsuccessful transaction! User trying to withdraw ${amount} that was more than the actual balance in the acount.\n")
            return print(f"Unsuccessful transaction!!! \nYou don't have enough money.\nYour Balance is ${self.balance}")

    def print_transactions(self):
        for line in self.transactions:
            print(line)

def main():
    atm = atm_account()

    while True:
        user_input = input("What would you like to do (deposit, withdraw, check balance, history, exit)? ")

        if user_input == 'exit':
            print('Thank you for being our loyal customer.\ngoodbye..')
            break

        elif user_input == 'deposit':
            user_to_deposit = int(input('howt much would you like to deposit? '))
            atm.deposit(user_to_deposit)

        elif user_input == 'check balance':
            print(f'Balance: ${atm.check_blance()}')
        

        elif user_input == 'withdraw':
            user_to_withdraw = int(input('how much would you like to withdraw? '))
            atm.withdraw(user_to_withdraw)
        

        elif user_input == 'history':
            atm.print_transactions()
main()

