with open('inputs/24.txt') as f:
    data = f.read().splitlines()

data = [line.replace('e', 'e ').replace('w', 'w ').split() for line in data]

black_points = set()

# Part A
for line in data:
    x = y = 0
    for pos in line:
        if pos == 'e':
            x += 2
        elif pos == 'w':
            x -= 2
        elif pos == 'nw':
            x -= 1
            y -= 1
        elif pos == 'ne':
            x += 1
            y -= 1
        elif pos == 'sw':
            x -= 1
            y += 1
        elif pos == 'se':
            x += 1
            y += 1
    point = (x, y)
    if point not in black_points:
        black_points.add(point)
    else:
        black_points.remove(point)

print(len(black_points))

def get_adjacent_black(p) -> int:
    adjacent_points = [
        (p[0]-1, p[1]-1), (p[0]+1, p[1]-1), (p[0]+2, p[1]), (p[0]+1, p[1]+1),
        (p[0]-1, p[1]+1), (p[0]-2, p[1])
    ]
    return len([1 for adj_point in adjacent_points if adj_point in black_points])


for i in range(100):
    new_blacks = set(black_points)
    for point in black_points:
        num_adjacent_black = get_adjacent_black(point)
        if num_adjacent_black == 0 or num_adjacent_black > 2:
            new_blacks.remove(point)
    for x in range(-(35+i), 35+i):
        for y in range(-(35+i), 35+i):
            point = (x, y)
            if point not in black_points:
                num_adjacent_black = get_adjacent_black(point)
                if num_adjacent_black == 2:
                    new_blacks.add(point)
    black_points = new_blacks

print(len(black_points))
