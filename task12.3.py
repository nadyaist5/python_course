class Groceries:

    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

    def __purchase_account(self):
        print('A purchase was completed.')

    def buy_vegetables(self):
        self.__purchase_account()
        print('You bought', self.amount, 'gramms of', self.type)

purchase_1 = Groceries('potatoes', 2000)
purchase_1.buy_vegetables()