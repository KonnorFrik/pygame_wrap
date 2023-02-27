# TODO write a add/sub/mul/div methods for ??
# TODO Make a 'x' and 'y' numpy array for ??
import pygame as pg


class BasePosition:
    """Hold a x and y val
        Represent a position of object"""

    def __init__(self, x: int = None, y: int = None):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x={self.x} y={self.y}"


class BaseObject:
    def __init__(self,
                 screen,
                 color: tuple[int],
                 x: int = 0,
                 y: int = 0,
                 width: int = 0,
                 height: int = 0,
                 border: int = 0,
                 *args,
                 **kwargs):

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



class IBaseSprite(pg.sprite.Sprite):
    def __init__(self,
                 screen = None,
                 x: int = 0,
                 y: int = 0,
                 width: int = 0,
                 height: int = 0,
                 filename: str = None,
                 *args,
                 **kwargs):

        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.filename = filename


    def render(self):
        """Draw object on screen"""
        ...

    def update(self):
        """Update object logic here per tick"""
        ...

    def refresh(self):
        """Call update for first, render after"""
        self.update()
        self.render()
