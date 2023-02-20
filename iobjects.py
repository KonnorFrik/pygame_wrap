import math


class BasePosition:
    """Hold a x and y val
        Represent a position of object"""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class BaseObject:
    def __init__(self,
                 screen,
                 color: tuple[int],
                 x: int = 0,
                 y: int = 0,
                 width: int = 0,
                 height: int = 0,
                 border: int = 0):

        self.screen = screen
        self.color = color
        self.pos = BasePosition(x, y)
        self.width = width
        self.height = height
        self.border = border
        self.draw = None

    def render(self):
        """Draw object on screen"""
        ...

    def update(self):
        """Update object logic here per loop"""
        ...

    def refresh(self):
        """Call update for first, render after"""
        self.update()
        self.render()




class Angle(int):
    def __init__(self, degrees: int, *a, **kw):
        super().__init__()
        self.angle = degrees


    def __add__(self, other: int):
        if (self.angle + other) > 360:
            return Angle(360 - self.angle)

        else:
            return Angle(self.angle + other)


    def __sub__(self, other: int):
        if (self.angle - other) < 0:
            return  Angle(360 - self.angle)

        else:
            return Angle(self.angle - other)

