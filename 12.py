import numpy as np

with open('inputs/12.txt') as f:
    data = f.read().split('\n')

# Part A
position = np.array([0, 0])  # Vector [east, north]
direct_i = 0
directions = ['E', 'S', 'W', 'N']

def go(direct: str) -> np.ndarray:
    move: np.ndarray
    if direct == 'N':
        move = np.array([0, 1])
    elif direct == 'S':
        move = np.array([0, -1])
    elif direct == 'E':
        move = np.array([1, 0])
    else:
        move = np.array([-1, 0])
    return move


for line in data:
    direction = line[0]
    steps = int(line[1:])
    if direction == 'R':
        direct_i = (direct_i + steps // 90) % 4
    elif direction == 'L':
        direct_i = (direct_i - steps // 90) % 4
    else:
        if direction == 'F':
            direction = directions[direct_i]
        position += steps * go(direction)

print(np.sum(np.abs(position)))

# Part B
def rotate(vector: np.ndarray, degrees: int, left: bool) -> np.ndarray:
    counter_clockwise = 1 if left else -1
    angle = np.radians(counter_clockwise * degrees)
    rotation_matrix = np.array([
        [np.cos(angle), -1 * np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    return np.round(rotation_matrix @ vector).astype(np.int)


# Vectors [east, north]
position = np.array([0, 0])
waypoint = np.array([10, 1])

for line in data:
    direction = line[0]
    steps = int(line[1:])
    if direction in 'NSWE':
        waypoint += steps * go(direction)
    elif direction == 'R':
        waypoint = rotate(waypoint, steps, left=False)
    elif direction == 'L':
        waypoint = rotate(waypoint, steps, left=True)
    elif direction == 'F':
        position += steps * waypoint

print(np.sum(np.abs(position)))
