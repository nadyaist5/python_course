class Table:

    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.length, self.width, self.height)


class Kitchen(Table):
    def how_places(self, n):
        if n < 2:
            print('It is not kitchen table')
        else:
            self.places = n

    def out_places(self):
        print(self.places)


class Transformer(Table):
    def transform(self):
        self.height = self.height / 5.0
        self.length = self.length / 2.0

    def volume(self):
        print('Volume is', self.height * self.length * self.width)


t_room1 = Kitchen(2, 1, 0.5)
t_room1.outing()
t_room1.how_places(5)
t_room1.out_places()
t_room2 = Table(1, 3, 0.7)
t_room2.outing()
t_room3 = Transformer(3, 1, 1.5)
t_room3.volume()
t_room3.transform()
t_room3.outing()
t_room3.volume()