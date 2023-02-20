import math


def radians(degrees: int) -> float | int:
    return degrees * (math.pi / 180)


def endpoint(x: int, y: int, length: int, angle: int) -> tuple[int]:
    angle_radians = radians(angle)
    new_x = x + round(length * math.sin(angle_radians))
    new_y = y + round(length * math.cos(angle_radians))
    return new_x, new_y

