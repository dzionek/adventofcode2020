from collections import Counter

file = open('inputs/2.txt')
data = [
    [
        element.strip('\n').strip(':')
        for element in line.split(' ')
    ]
    for line in file.readlines()
]

# Part A - O(n)
valid = 0
for line in data:
    minimum, maximum = line[0].split('-')
    counter = Counter(line[2])
    if int(minimum) <= counter[line[1]] <= int(maximum):
        valid += 1
print(valid)

# Part B - O(n)
valid = 0
for line in data:
    first, second = line[0].split('-')
    letter = line[1]
    how_many = 0
    if line[2][int(first) - 1] == letter:
        how_many += 1
    if line[2][int(second) - 1] == letter:
        how_many += 1
    if how_many == 1:
        valid += 1
print(valid)