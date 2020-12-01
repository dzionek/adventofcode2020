file = open('inputs/1.txt')
data_set = {int(element) for element in file.readlines()}

# Part A - O(n)
print([a * (2020 - a) for a in data_set if 2020 - a in data_set][0])

# Part B - O(n^2)
print([a * b * (2020 - a - b) for a in data_set for b in data_set
       if 2020 - a - b in data_set][0])
