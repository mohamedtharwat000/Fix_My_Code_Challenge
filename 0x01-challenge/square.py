#!/usr/bin/python3
"""Square class."""


class Square():
    """Square class."""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """__init__ constructor."""
        for key, value in kwargs.items():
            setattr(self, key, value)

        if self.width == 0 and self.height != 0:
            self.width = self.height

    def area_of_my_square(self):
        """Area of the square."""
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Permiter of the square."""
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """Represent the square."""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
