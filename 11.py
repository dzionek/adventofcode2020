from typing import List

with open('inputs/11.txt') as f:
    data_input = f.read().split('\n')

num_occupied = 0
num_new_round = 1
width = len(data_input[0])
height = len(data_input)

# Part A
data = data_input[:]
while num_new_round:
    num_new_round = 0
    data_round = data[:]
    for i in range(height):
        for j in range(width):
            num_occupied_adjacent = 0
            if i > 0 and j > 0 and data_round[i-1][j-1] == '#':
                num_occupied_adjacent += 1
            if i > 0 and data_round[i-1][j] == '#':
                num_occupied_adjacent += 1
            if i > 0 and j < width-1 and data_round[i-1][j+1] == '#':
                num_occupied_adjacent += 1
            if j > 0 and data_round[i][j-1] == '#':
                num_occupied_adjacent += 1
            if j < width-1 and data_round[i][j+1] == '#':
                num_occupied_adjacent += 1
            if i < height-1 and j > 0 and data_round[i+1][j-1] == '#':
                num_occupied_adjacent += 1
            if i < height-1 and data_round[i+1][j] == '#':
                num_occupied_adjacent += 1
            if i < height-1 and j < width-1 and data_round[i+1][j+1] == '#':
                num_occupied_adjacent += 1

            if data[i][j] == 'L' and num_occupied_adjacent == 0:
                data[i] = data[i][:j] + '#' + data[i][j+1:]
                num_new_round += 1
            elif data[i][j] == '#' and num_occupied_adjacent >= 4:
                data[i] = data[i][:j] + 'L' + data[i][j+1:]
                num_new_round += 1
    data_round = data

print(sum([row.count('#') for row in data]))

# Part B
def how_many_see(data_round: List[str], i: int, j: int) -> int:
    occupied = 0

    # left
    x = j
    if x != 0:
        x -= 1
        while True:
            if data_round[i][x] == '#':
                occupied += 1
                break
            elif data_round[i][x] == 'L':
                break
            if x == 0:
                break
            x -= 1

    # right
    x = j
    if x != width - 1:
        x += 1
        while True:
            if data_round[i][x] == '#':
                occupied += 1
                break
            elif data_round[i][x] == 'L':
                break
            if x == width - 1:
                break
            x += 1

    # down
    y = i
    if y != height - 1:
        y += 1
        while True:
            if data_round[y][j] == '#':
                occupied += 1
                break
            elif data_round[y][j] == 'L':
                break
            if y == height - 1:
                break
            y += 1

    # up
    y = i
    if y != 0:
        y -= 1
        while True:
            if data_round[y][j] == '#':
                occupied += 1
                break
            elif data_round[y][j] == 'L':
                break
            if y == 0:
                break
            y -= 1

    # left up
    y = i
    x = j
    if y != 0 and x != 0:
        y -= 1
        x -= 1
        while True:
            if data_round[y][x] == '#':
                occupied += 1
                break
            elif data_round[y][x] == 'L':
                break
            if y == 0 or x == 0:
                break
            y -= 1
            x -= 1

    # right up
    y = i
    x = j
    if y != 0 and x != width-1:
        y -= 1
        x += 1
        while True:
            if data_round[y][x] == '#':
                occupied += 1
                break
            elif data_round[y][x] == 'L':
                break
            if y == 0 or x == width-1:
                break
            y -= 1
            x += 1

    # left down
    y = i
    x = j
    if y != height-1 and x != 0:
        y += 1
        x -= 1
        while True:
            if data_round[y][x] == '#':
                occupied += 1
                break
            elif data_round[y][x] == 'L':
                break
            if y == height-1 or x == 0:
                break
            y += 1
            x -= 1

    # right down
    y = i
    x = j
    if y != height-1 and x != width-1:
        y += 1
        x += 1
        while True:
            if data_round[y][x] == '#':
                occupied += 1
                break
            elif data_round[y][x] == 'L':
                break
            if y == height-1 or x == width-1:
                break
            y += 1
            x += 1

    return occupied


num_occupied = 0
num_new_round = 1

data = data_input[:]
while num_new_round:
    num_new_round = 0
    data_round = data[:]
    for i in range(height):
        for j in range(width):
            num_occupied_adjacent = how_many_see(data_round, i, j)

            if data[i][j] == 'L' and num_occupied_adjacent == 0:
                data[i] = data[i][:j] + '#' + data[i][j+1:]
                num_new_round += 1
            elif data[i][j] == '#' and num_occupied_adjacent >= 5:
                data[i] = data[i][:j] + 'L' + data[i][j+1:]
                num_new_round += 1
    data_round = data
print(sum([row.count('#') for row in data]))