class Cat:

    def __init__(self, name):
        self.name = name
        self.__age = 2.3
        self.__favourite_toy = 'little fish'

    def get_favourite_toy(self):
        return self.__favourite_toy

    def __make_happy(self, toy):
        if toy == self.__favourite_toy:
            print('Cat is happy!')
        else:
            print("Cat isn't happy")

    def set_age(self, age):
        if 1 < age < 30:
            self.__age = age
        else:
            print("It's not the age")

    def set_favourite_toy(self, toy):
        if type(toy) == str:
            self.__favourite_toy = toy
        else:
            print("It's not a toy")

    def get_age(self):
        return self.__age

    def show_info(self):
        print(self.__age, 'years old cat', self.name)
        self.__make_happy('pig')

cat_1 = Cat('Simon')
cat_1.show_info()
cat_2 = Cat('Billy')
cat_2.set_age(1.5)
cat_2.set_favourite_toy(123)
cat_2.set_favourite_toy('pig')
cat_2.show_info()