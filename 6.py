file = open('inputs/6.txt')
data = file.read().split('\n\n')

# Part A
print(sum([len(set(el.replace('\n', ''))) for el in data]))

# Part B
res = sum([
    sum([
        el.replace('\n', '').count(letter) == el.count('\n') + 1
        for letter in set(el.replace('\n', ''))
    ])
    for el in data
])

print(res)
