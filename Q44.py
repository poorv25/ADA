import math

def distance(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0
    elif x1 == x2:
        return abs(y2 - y1)
    elif y1 == y2:
        return abs(x2 - x1)
    else:
        mid_x = (x1 + x2) / 2
        left_distance = distance(x1, y1, mid_x, y2)
        right_distance = distance(mid_x, y1, x2, y2)
        return math.sqrt(left_distance ** 2 + right_distance ** 2)
