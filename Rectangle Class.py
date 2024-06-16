class Point:
    """ A class to represent a point in 2D space """

    def __init__(self, x, y):
        """ Initialize point at x, y """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


class Rectangle:
    """ A class to represent a rectangle """

    def __init__(self, pos, w, h):
        """ Initialize rect at x, y with width w and height h"""
        self.corner = pos
        self.width = w
        self.height = h

    def __str__(self):
        """ Return string representation of rectangle """
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)


def create_rectangle(x, y, w, h):
    """ Create a rectangle at x, y with width w and height h"""
    return Rectangle(Point(x, y), w, h)


def str_rectangle(rect):
    """ Return a string representation of a rectangle """
    return "({0}, {1}, {2})".format(rect.corner, rect.width, rect.height,)


def shift_rectangle(rect, dx, dy):
    """ Shift a rectangle by dx and dy """
    rect.corner.x += dx
    rect.corner.y += dy


def offset_rectangle(rect, dx, dy):
    """ Shift a rectangle by dx and dy """
    new_corner = Point(rect.corner.x + dx, rect.corner.y + dy)
    return Rectangle(new_corner, rect.width, rect.height)

"""Testing the functions"""
r1 = create_rectangle(10, 20, 30, 40)
print(str_rectangle(r1))
shift_rectangle(r1, -10, -20)
print(str_rectangle(r1))
r2 = offset_rectangle(r1, 100, 100)
print(str_rectangle(r1))  # Should be the same as previous
print(str_rectangle(r2))
