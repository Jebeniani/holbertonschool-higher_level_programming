#!/usr/bin/python3
"""writing class Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """creating square class inherited from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """attributes updates"""
        my_list = ["id", "size", "x", "y"]
        if args is None or not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for arg in range(len(args)):
                setattr(self, my_list[arg], args[arg])

    def to_dictionary(self):
        """method that returns the dictionary representation of a Square"""
        return dict(id=self.id, size=self.width, x=self.x, y=self.y)
