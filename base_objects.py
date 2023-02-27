import pygame as pg
from . import iobjects
from . import mymath
import math
from copy import deepcopy


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
        self.end_pos = iobjects.BasePosition(x=self.width, y=self.height)
        self.draw = pg.draw.line


    def render(self):
        self.draw(self.screen,
                  self.color,
                  [self.pos.x,
                   self.pos.y,
                   ],
                  [self.end_pos.x,
                   self.end_pos.y,
                   ],
                  self.border)


class Angle:
    def __init__(self, angle: int):
        self.angle = angle

    def set(self, other):
        self.angle = other
        self.__check()

    def copy(self):
        return deepcopy(self)

    def opposite(self):
        copy = self.copy()
        copy -= 180
        return copy


    def __check(self):
        while self.angle < 0 or self.angle > 360:

            if self.angle > 360:
                self.angle -= 360

            if self.angle < 0:
                self.angle = 360 - abs(self.angle)


    def __str__(self):
        return f"Angle: {self.angle}"


    def __add__(self, other):
        copy = self.copy()
        copy.angle += other
        copy.__check()
        return copy


    def __sub__(self, other):
        copy = self.copy()
        copy.angle -= other
        copy.__check()
        return copy


    def __mul__(self, other):
        copy = self.copy()
        copy.angle *= other
        copy.__check()
        return copy


    def __floordiv__(self, other):
        copy = self.copy()
        copy.angle //= other
        copy.__check()
        return copy


    def __truediv__(self, other):
        copy = self.copy()
        copy.angle /= other
        copy.__check()
        return copy


    def __mod__(self, other):
        copy = self.copy()
        copy.angle %= other
        copy.__check()
        return copy


class Vector(object):
    def __init__(self, x: int = 0, y: int = 0, length: int = 0, angle: int = 0, *a, **kw):
        self.pos = iobjects.BasePosition(x=x, y=y)
        self.end_pos = iobjects.BasePosition()
        self.length = length
        #self.angle = angle
        self.angle = Angle(angle)
        self._calc_endpoint()


    def _calc_endpoint(self):
        self.end_pos.x, self.end_pos.y = mymath.endpoint(x=self.pos.x, y=self.pos.y, length=self.length, angle=self.angle.angle)


    def copy(self):
        return self
        #return deepcopy(self)


    def update_length(self):
        self.length = mymath.length_by_points(x1=self.pos.x,
                                              y1=self.pos.y,
                                              x2=self.end_pos.x,
                                              y2=self.end_pos.y)


    def __add__(self, other):
        copy = self.copy()

        if isinstance(other, int):
            copy.length += other
            copy._calc_endpoint()
            return copy

        elif isinstance(other, Vector):
            other.pos.x = copy.end_pos.x
            other.pos.y = copy.end_pos.y
            other._calc_endpoint()

            copy.end_pos.x = other.end_pos.x
            copy.end_pos.y = other.end_pos.y

            copy.update_length()

            copy.angle.set(mymath.angle_by_point(x1=copy.pos.x,
                                                 y1=copy.pos.y,
                                                 x2=copy.end_pos.x,
                                                 y2=copy.end_pos.y))

            #copy._calc_endpoint()
            return copy


    def __sub__(self, other):
        copy = self.copy()
        if isinstance(other, int):
            copy.length -= other
            copy._calc_endpoint()
            return copy

        elif isinstance(other, Vector):
            return copy + (-other)


    def __neg__(self):
        copy = self.copy()
        copy.pos.x, copy.end_pos.x = copy.end_pos.x, copy.pos.x
        copy.pos.y, copy.end_pos.y = copy.end_pos.y, copy.pos.y
        copy.angle = copy.angle.opposite()
        return copy


    def __mul__(self, other):
        copy = self.copy()
        if isinstance(other, int):
            copy.length *= other
            copy._calc_endpoint()
            return copy

        elif isinstance(other, Vector):
            raise NotImplementedError


    def __truediv__(self, other):
        copy = self.copy()
        if isinstance(other, int):
            copy.length /= other
            copy._calc_endpoint()
            return copy

        elif isinstance(other, Vector):
            raise NotImplementedError


    def __floordiv__(self, other):
        copy = self.copy()
        if isinstance(other, int):
            copy.length //= other
            copy._calc_endpoint()
            return copy

        elif isinstance(other, Vector):
            raise NotImplementedError


    def __str__(self):
        return f"Vector: (x={self.pos.x}, y={self.pos.y},\n\tend x={self.end_pos.x}, end y={self.end_pos.y},\n\tlen={self.length}, angle={self.angle}"


class VectorLine(Vector, Line):
    def __init__(self, *a, **kw):
        super(Vector, self).__init__(*a, **kw)
        super().__init__(*a, **kw)


class BaseSprite(iobjects.IBaseSprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.image = None

        if self.filename:
            self.image = pg.image.load(self.filename).convert_alpha()

        else:
            self.image = pg.Surface((self.width, self.height))

        self.rect = self.image.get_rect(x=self.x, y=self.y)


    def render(self):
        """Draw object on screen"""
        self.screen.blit(self.image, self.rect)


