import math


def radians(degrees: int) -> float | int:
    return degrees * (math.pi / 180)


def endpoint(x: int, y: int, length: int, angle: int) -> tuple[int]:
    angle_radians = math.radians(angle)
    new_x = x + round(length * math.cos(angle_radians))
    new_y = y + round(length * math.sin(angle_radians))
    return new_x, new_y


def length_by_points(x1: int, y1: int, x2: int, y2: int) -> int:
    return int(math.dist((x1,y1), (x2, y2)))


def angle_by_point(x1: int, y1: int, x2: int, y2: int) -> int | float:
    try:
        result = math.degrees(math.atan((y2-y1)/(x2-x1)))

    except ZeroDivisionError:
        result = 90

    return result

