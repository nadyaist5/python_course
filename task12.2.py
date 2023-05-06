class BankAccount:

    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number
        self.__balance = 238653
        self.__password = 2913

    def get_password(self):
        return self.__password

    def set_balance(self, password, balance):
        if password == self.__password:
            self.__balance = balance

    def get_balance(self):
        return self.__balance

    def show_info(self):
        print('The balance of the account', self.account_number, 'ownered by', self.owner, 'is', self.__balance, 'rubles.')

account_1 = BankAccount('Nadya', 12345678)
account_1.set_balance(2913, 1000000)
account_1.show_info()


