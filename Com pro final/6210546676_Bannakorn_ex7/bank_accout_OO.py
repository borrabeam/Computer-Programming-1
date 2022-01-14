class BankAccount():
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        self.__data = [self.__name, self.__balance]

    def __str__(self):
        return f"['{self.__data[0]}', {self.__data[1]}]"

    @property
    def get_name(self):
        return self.__data[0]

    @property
    def get_balance(self):
        return self.__data[1]
        

class BankData():

    def __init__(self):
        self.bank_account_DB = {}
        self.create_account()

    def create_account(self):
        import random
        for i in range(10):
            account_ID = str(random.randint(1000, 9999))
            accout_name = 'account' + str(i)
            balance = random.randint(20, 2000)
            self.bank_account_DB[account_ID] = BankAccount(accout_name, balance)
            # account = BankAccount(account_ID, accout_name, balance)
            # self.account_DB.append(account)

    def search(self, account_id):
            if account_id in self.bank_account_DB:
                return True
            else: 
                return False

    def deposit(self, account_id, amoumt):
        if self.search(account_id) != False:
            self.bank_account_DB[int(account_id)].balance += amoumt
        else:
            print('Record not found.')

    def withdraw(self, account_id, amount):
        if not self.search(account_id):
            print('Record not found.')
        else:
            if self.bank_account_DB[int(account_id)].balance < amount:
                print('Insufficient funds. Transacion aborted.')
            else:
                self.bank_account_DB[int(account_id)].balance -= amount

    def display(self):
        for entry in self.bank_account_DB:
            print(entry + ':' + str(self.bank_account_DB[entry]))

            
    # def get_account(self):
    #     index = self.search(account_id)
    #     return self.bank_account_DB

def menu():
    print('Banking System Menu:')
    print('Press 1 to display all records.')
    print('Press 2 to search for a record')
    print('Press 3 to deposit amount')
    print('Press 4 to withdraw amount')
    print('Press 0 to exit')

menu()
choice = input('Enter a choice (0-4): ')
bank_data = BankData()
while choice != '0':

    
    if choice == '1':
        bank_data.display()
        menu()
    elif choice == '2':
        search_account = input('Enter an account number to search: ')
        
        if bank_data.search(search_account) == True:
            # print(bank_data.get_account(search_account))
            print(search_account + ':' + str(bank_data.bank_account_DB[search_account]))
            menu()
        else:
            print('Record not found.')
            menu()
    elif choice == '3':
        deposit_account = input('Enter an account number to deposit: ')
        deposit_amount = float(input('Enter an amount to deposit: '))
        bank_data.deposit(deposit_account, deposit_amount)
        menu()
    elif choice == '4':
        withdraw_account = input('Enter an account number to withdraw: ')
        withdraw_amount = float(input('Enter an amount to withdraw: '))
        bank_data.withdraw(withdraw_account, withdraw_amount)
        menu()
    else:
        print('Invalid choice selection. Please try again')
        menu()
    choice = input('Enter a choice (0-4): ')