import pygame as pg
from . import iobjects
from . import mymath
import math


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


    def __check(self):
        while self.angle < 0 or self.angle > 360:

            if self.angle > 360:
                self.angle -= 360

            if self.angle < 0:
                self.angle = 360 - abs(self.angle)


    def __str__(self):
        return f"Angle: {self.angle}"


    def __add__(self, other):
        self.angle += other
        self.__check()
        return self


    def __sub__(self, other):
        self.angle -= other
        self.__check()
        return self


    def __mul__(self, other):
        self.angle *= other
        self.__check()
        return self


    def __floordiv__(self, other):
        self.angle //= other
        self.__check()
        return self


    def __truediv__(self, other):
        self.angle /= other
        self.__check()
        return self


    def __mod__(self, other):
        self.angle %= other
        self.__check()
        return self


class Vector:
    def __init__(self, x: int, y: int, length: int, angle: int, *a, **kw):
        self.pos = iobjects.BasePosition(x=x, y=y)
        self.end_pos = iobjects.BasePosition()
        self.length = length
        #self.angle = angle
        self.angle = Angle(angle)
        self._calc_endpoint()


    def _calc_endpoint(self):
        self.end_pos.x, self.end_pos.y = mymath.endpoint(x=self.pos.x, y=self.pos.y, length=self.length, angle=self.angle.angle)


    def radians_angle(self) -> float:
        return math.radians(self.angle)


    def __add__(self, other):
        if isinstance(other, int):
            self.length += other
            self._calc_endpoint()
            return self

        elif isinstance(other, Vector):
            other.pos.x = self.end_pos.x
            other.pos.y = self.end_pos.y
            other._calc_endpoint()

            self.end_pos.x = other.end_pos.x
            self.end_pos.y = other.end_pos.y

            self.length = mymath.length_by_points(x1=self.pos.x,
                                                 y1=self.pos.y,
                                                 x2=self.end_pos.x,
                                                 y2=self.end_pos.y)

            #self.angle.anlge = mymath.angle_by_point(x1=self.pos.x,
                                                 #y1=self.pos.y,
                                                 #x2=self.end_pos.x,
                                                 #y2=self.end_pos.y)


            self._calc_endpoint()
            return self


    def __sub__(self, other):
        if isinstance(other, int):
            self.length -= other
            self._calc_endpoint()
            return self

        elif isinstance(other, Vector):
            return self + (-other)


    def __neg__(self):
        self.pos.x, self.end_pos.x = self.end_pos.x, self.pos.x
        self.pos.y, self.end_pos.y = self.end_pos.y, self.pos.y
        return self


    def __mul__(self, other):
        raise NotImplementedError


    def __div__(self, other):
        raise NotImplementedError



    def __str__(self):
        return f"Vector: (x={self.pos.x}, y={self.pos.y},\n\tend x={self.end_pos.x}, end y={self.end_pos.y},\n\tlen={self.length}, angle={self.angle}"


class VectorLine(Vector, Line):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        super(Vector, self).__init__(*a, **kw)

