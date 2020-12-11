from itertools import combinations

with open('inputs/9.txt') as f:
    data = [int(i) for i in f.read().split('\n')]

# Part A
num = 0

for num_index in range(25, len(data)):
    num = data[num_index]
    rest = data[0 if num_index - 25 < 0 else num_index - 25:num_index]
    valid = False
    for c in combinations(rest, 2):
        if sum(c) == num:
            valid = True

    if not valid:
        break

print(num)

# Part B
for i in range(0, len(data) - 1):
    s = [data[i]]
    for j in range(i+1, len(data)):
        s.append(data[j])
        if sum(s) == num:
            print(max(s) + min(s))
            exit()
        elif sum(s) > num:
            break
