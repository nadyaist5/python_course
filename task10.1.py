class Fridge:
    is_empty = True

    def __init__(self, size, color, place):
        self.size = size
        self.color = color
        self.place = place


class Human:

    def __init__(self, name):
        self.name = name

    def buy_food(self, fridge):
        if fridge.is_empty:
            fridge.is_empty = False
            print(fridge.size, fridge.color, "fridge in the ", fridge.place, " is full. ", self.name, " filled it.")
        else:
            print(fridge.size, fridge.color, "fridge in the ", fridge.place, " is already full.")

fridge_1 = Fridge('Big', 'Red', 'Kitchen')
fridge_2 = Fridge('Small', 'Black', 'Bedroom')
fridge_3 = Fridge('Big', 'White', 'Garage')

humans = [Human('Nadya'), Human('Yura')]

humans[0].buy_food(fridge_2)
