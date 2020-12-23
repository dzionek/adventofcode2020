with open('inputs/23.txt') as f:
    data = [int(c) for c in f.read().strip()]

n = len(data)
maxi = max(data)
mini = min(data)

clockwise = {el: data[(i+1) % n] for i, el in enumerate(data)}

def move(current: int) -> int:
    a = clockwise[current]
    b = clockwise[a]
    c = clockwise[b]
    clockwise[current] = clockwise[c]

    destination = current
    while destination in map(int, [a, b, c, current]):
        destination -= 1
        if destination < mini:
            destination = maxi

    temp = clockwise[destination]
    clockwise[destination] = a
    clockwise[c] = temp
    return clockwise[current]


# Part A
curr = data[0]
for _ in range(100):
    curr = move(curr)

line = ""
i = 1
while clockwise[i] != 1:
    line += str(clockwise[i])
    i = clockwise[i]

print(line)

# Part B
extra_data = [maxi+1+i for i in range(1000000-n)]
data.extend(extra_data)
n = len(data)
mini = min(data)
maxi = max(data)
clockwise = {el: data[(i+1) % n] for i, el in enumerate(data)}

curr = data[0]
for _ in range(10000000):
    curr = move(curr)

first_clockwise = clockwise[1]
second_clockwise = clockwise[first_clockwise]
print(first_clockwise * second_clockwise)
