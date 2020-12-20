import numpy as np
from common_20 import all_transformations, transform

with open('inputs/20_monster.txt') as f:
    monster_pattern = f.read().splitlines()

with open('inputs/20_b.txt') as f:
    image = []
    for square in f.read().split('\n\n'):
        for row in square.splitlines()[1:-1]:
            parts = row.split(' ')
            for i, part in enumerate(parts):
                parts[i] = part[1:-1]
            image.append(''.join(parts))

image = np.array([[c for c in row] for row in image])

points = []
for i in range(len(monster_pattern)):
    for j in range(len(monster_pattern[0])):
        if monster_pattern[i][j] == '#':
            points.append((i, j))

first = points.pop()
other_relative = [
    (point[0] - first[0], point[1] - first[1])
    for point in points
]

res = 0
for (t_a, t_b) in all_transformations:
    new_image = transform(t_a, t_b, image)
    for i in range(len(new_image)):
        for j in range(len(new_image[0])):
            if new_image[i][j] == '#':
                try:
                    if all([
                        new_image[i+point[0]][j+point[1]] == '#'
                        for point in other_relative
                    ]):
                        res += 1
                except IndexError:
                    continue

print(sum(sum(c == '#' for c in line) for line in image) - res*(len(points)+1))
