

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5


    def get_perimeter(self):
        return 2 * self.width + 2 * self.height 

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            pic = '*' * self.width + '\n'
            pic = pic * self.height
            return pic

    def get_amount_inside(self, shape):
        return self.width * self.height / shape.get_area()

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side







