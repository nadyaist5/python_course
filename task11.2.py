class Figure:
    color = "white"

    def change_color(self, color):
        self.color = color

    def out_params(self):
        pass

class Oval(Figure):

    def __init__(self, radius1, radius2):
        self.radius1 = radius1
        self.radius2 = radius2

    def out_params(self):
        print(self.color, self.radius1, self.radius2)


class Square(Figure):

    def __init__(self, side):
        self.side = side

    def out_params(self):
        print(self.color, self.side)

figure_1 = Oval(3, 2)
figure_1.change_color('blue')
figure_1.out_params()
figure_2 = Square(4)
figure_2.change_color('pink')
figure_2.out_params()
