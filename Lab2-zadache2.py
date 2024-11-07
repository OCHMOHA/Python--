#оушен
#нбибд-01-24
#лаб 2 билет 27
# python
#задача 2
import math
def are_points_collinear(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return area == 0

are_points_collinear(1, 2, 2, 4, 3, 6)
