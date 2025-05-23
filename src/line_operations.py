from pathlib import Path
import math
from shapely.geometry import LineString


def merge_lines(lines: list[LineString]):
    temp_set = set(lines)
    any_new = True
    
    combinations = pair_not_equals(temp_set)
    while any_new and combinations:
        for combination in combinations:
            line0, line1 = combination
            any_new, merged = merge_two_lines(line0, line1)
            if any_new:
                temp_set.remove(line0)
                temp_set.remove(line1)
                temp_set.add(merged)
                combinations = pair_not_equals(temp_set)
                break

    return list(temp_set)

def pair_not_equals(lines):
    return list([(line0, line1) 
                        for line0 in lines 
                        for line1 in lines if line1 != line0])


def merge_two_lines(ls0, ls1) -> tuple[bool, LineString|None]:
    paralel = are_paralel(ls0, ls1)
    near = ends_near(ls0, ls1)

    if near and paralel:
        dx0, dy0 = d_x_d_y(ls0)
        dx1, dy1 = d_x_d_y(ls1)
        max_dx = max(abs(dx0), abs(dx1))
        max_dy = max(abs(dy0), abs(dy1))
        point4 = [ls0.coords[0], ls0.coords[1], ls1.coords[0], ls1.coords[1]] 
        s = []
        s = sorted(point4, key=lambda p: p[0]) if max_dx > max_dy else sorted(point4, key=lambda p: p[1])
        x0 = (s[0][0] + s[1][0])/2
        y0 = (s[0][1] + s[1][1])/2
        x1 = (s[2][0] + s[3][0])/2
        y1 = (s[2][1] + s[3][1])/2
        ls_created = LineString([(x0, y0), (x1, y1)])
        return (True, ls_created)
    else:
        return (False, None)

def d_x_d_y(line: LineString) -> tuple[float, float]:
    x0, y0 = line.coords[0]
    x1, y1 = line.coords[1]
    return (x1 - x0, y1 - y0)

def d_x(line: LineString):
    x0, _ = line.coords[0]
    x1, _ = line.coords[1]
    return x1 - x0

def d_y(line: LineString):
    _, y0 = line.coords[0]
    _, y1 = line.coords[1]
    return y1 - y0

def direction(line: LineString):
        x0, y0 = line.coords[0]
        x1, y1 = line.coords[1]
        theta = math.atan2(-(x1 - x0), y1 - y0)
        return theta

def ends_near(line0: LineString, line1: LineString, delta=3) -> bool:
    distance = line0.distance(line1)
    res = distance < delta
    return res

def are_paralel(line0: LineString, line1: LineString, rho_deg=1) -> bool:
    th0 = direction(line0)
    th1 = direction(line1)
    res = abs(th1 - th0) < math.pi*rho_deg/(180)
    return res

def to_shapely(line0) -> LineString:
    l0_x0 = int(line0[0])
    l0_y0 = int(line0[1])
    l0_x1 = int(line0[2])
    l0_y1 = int(line0[3])
    ls0 = LineString([(l0_x0, l0_y0), (l0_x1, l0_y1)])
    return ls0