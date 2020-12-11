with open('inputs/10.txt') as f:
    data = [int(i) for i in f.read().split('\n')]

# Part A
difference1 = 0
difference3 = 0
jolt = 0

while True:
    if jolt + 1 in data:
        difference1 += 1
        jolt += 1
    elif jolt + 2 in data:
        jolt += 2
    elif jolt + 3 in data:
        jolt += 3
        difference3 += 1
    else:
        break

difference3 += 1
print(difference1 * difference3)

# Part B
res = [0] * (max(data) + 1)
res[0] = 1
if 1 in data:
    res[1] = 1
if 2 in data:
    res[2] = 2 if 1 in data else 1

for el in sorted([el for el in data if el > 2]):
    res[el] = res[el-1] + res[el-2] + res[el-3]

print(res[-1])
