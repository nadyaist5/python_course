class Box:
    content = []

    def put_in(self, Figure):
        self.content.append(Figure)

    def show_content(self):
        for f in self.content:
            if (isinstance(f, Ball)):
                print(f.radius, 'cm in radius', f.color, f.material, 'Ball')
            if (isinstance(f, Cube)):
                print(f.side, 'cm wide', f.color, f.material, 'Cube')
            if (isinstance(f, Pyramid)):
                print(f.side, 'cm wide and', f.height, 'cm high', f.color, f.material, 'Pyramid')


class Figure:
    color = ""
    material = ""


class Ball(Figure):
    radius = 0

    def __init__(self, radius, color, material):
        self.radius = radius
        self.color = color
        self.material = material


class Cube(Figure):
    side = 0

    def __init__(self, side, color, material):
        self.side = side
        self.color = color
        self.material = material


class Pyramid(Figure):
    side = 0
    height = 0

    def __init__(self, side, height, color, material):
        self.side = side
        self.height = height
        self.color = color
        self.material = material

ball_1 = Ball(3, 'Black', 'Wood')
ball_2 = Ball(1.5, 'Pink', 'Plastic')
cube_1 = Cube(4, 'Grey', 'Metal')
cube_2 = Cube(2, 'Green', 'Plastic')
pyramid_1 = Pyramid(1, 5, 'Blue', 'Rubber')
pyramid_2 = Pyramid(3, 1, 'Purple', 'Wood')
box = Box()

box.put_in(cube_2)
box.put_in(ball_1)
box.put_in(pyramid_2)

box.show_content()