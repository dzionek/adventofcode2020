file = open('inputs/6.txt')
data = file.read().split('\n\n')

# Part A
print(sum([len(set(el.replace('\n', ''))) for el in data]))

# Part B
print(sum([
    sum([
        el.rstrip().count(letter) == el.count('\n') + 1
        for letter in set(el.rstrip())
    ])
    for el in data
]))
