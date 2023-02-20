import pygame as pg
from . import iobjects
from . import mymath


class Circle(iobjects.BaseObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.draw = pg.draw.ellipse


    def render(self):
       self.draw(self.screen,
                 self.color,
                 [self.pos.x,
                  self.pos.y,
                  self.width,
                  self.height],
                 self.border)


class Box(iobjects.BaseObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.draw = pg.draw.rect


    def render(self):
        self.draw(self.screen,
                  self.color,
                  [self.pos.x,
                   self.pos.y,
                   self.width,
                   self.height],
                  self.border)


class Line(iobjects.BaseObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.end_x = self.width
        self.end_y = self.height
        self.draw = pg.draw.line


    def render(self):
        self.draw(self.screen,
                  self.color,
                  [self.pos.x,
                   self.pos.y,
                   ],
                  [self.end_x,
                   self.end_y,
                   ],
                  self.border)


class ALine(Line):
    def __init__(self, length: int, angle: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.length = length
        #self.angle = iobjects.Angle(angle)
        self.angle = angle
        self._calc_endpoint()

    def _calc_endpoint(self):
        self.end_x, self.end_y = mymath.endpoint(x=self.pos.x, y=self.pos.y, length=self.length, angle=self.angle)

