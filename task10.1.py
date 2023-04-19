class Fridge:
    is_empty = True
    size = ""
    color = ""
    place = ""

    def __init__(self, size, color, place):
        self.size = size
        self.color = color
        self.place = place


class Human:
    name = ""

    def __init__(self, name):
        self.name = name

    def buy_food(self, Fridge):
        if Fridge.is_empty:
            Fridge.is_empty = False
            print(Fridge.size, Fridge.color, "fridge in the ", Fridge.place, " is full. ", self.name, " filled it.")
        else:
            print(Fridge.size, Fridge.color, "fridge in the ", Fridge.place, " is already full.")

fridge_1 = Fridge('Big', 'Red', 'Kitchen')
fridge_2 = Fridge('Small', 'Black', 'Bedroom')
fridge_3 = Fridge('Big', 'White', 'Garage')

humans = [Human('Nadya'), Human('Yura')]

humans[0].buy_food(fridge_2)