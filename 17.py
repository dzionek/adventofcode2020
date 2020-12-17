from typing import Tuple, List, Dict
from copy import deepcopy
from itertools import product

turns = 6

with open('inputs/17.txt') as f:
    data = f.read().split('\n')

Point = Tuple[int, ...]
inp_size = len(data)

# Part A
points: Dict[Point, bool] = {
    (x, y, z): False
    for x in range(-(turns+1), (inp_size+turns+1))
    for y in range(-(turns+1), (inp_size+turns+1))
    for z in range(-(turns+1), turns+2)
}
for y, line in enumerate(data):
    for x, state in enumerate(line):
        if state == '#':
            points[(x, y, 0)] = True


def find_neighbors(p: Point, dim: int) -> List[Point]:
    options = list(product((-1, 0, 1), repeat=dim))
    options.remove(tuple([0] * dim))
    return [
        tuple(map(sum, zip(p, option)))
        for option in options
    ]


def get_next_items(points_dict: Dict[Point, bool], dim: int,
                   domain_points: List[Point]) -> Dict[Point, bool]:
    new_points = deepcopy(points_dict)
    for point in domain_points:
        is_active = points_dict[point]
        neighbors = find_neighbors(point, dim)
        how_many_active = len([
            1 for neighbor in neighbors if points_dict[neighbor]
        ])
        if not(is_active and 2 <= how_many_active <= 3):
            new_points[point] = False
        if (not is_active) and how_many_active == 3:
            new_points[point] = True
    return new_points


def get_next_a(i: int, points_dict: Dict[Point, bool]) -> Dict[Point, bool]:
    size = i + inp_size
    domain_points = [
        (x, y, z)
        for x in range(-i, size)
        for y in range(-i, size)
        for z in range(-i, (i+1))
    ]
    return get_next_items(points_dict, 3, domain_points)


j = 1
for _ in range(turns):
    points = get_next_a(j, points)
    j += 1
print(len([active for active in points.values() if active]))

# Part B
points: Dict[Point, bool] = {
    (x, y, z, q): False
    for x in range(-(turns+1), (inp_size+turns+1))
    for y in range(-(turns+1), (inp_size+turns+1))
    for z in range(-(turns+1), turns+2)
    for q in range(-(turns+1), turns+2)
}

for y, line in enumerate(data):
    for x, state in enumerate(line):
        if state == '#':
            points[(x, y, 0, 0)] = True

def get_next_b(i: int, points_dict: Dict[Point, bool]) -> Dict[Point, bool]:
    size = i + inp_size
    domain_points = [
        (x, y, z, q)
        for x in range(-i, size)
        for y in range(-i, size)
        for z in range(-i, (i+1))
        for q in range(-i, (i+1))
    ]
    return get_next_items(points_dict, 4, domain_points)


j = 1
for _ in range(turns):
    points = get_next_b(j, points)
    j += 1
print(len([active for active in points.values() if active]))
