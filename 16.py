import re
from math import prod

with open('inputs/16.txt') as f:
    data = f.read().split('\n\n')

# Part A
fields = data[0].split('\n')
fields_pattern = re.compile(r'\d+-\d+')
fields = [fields_pattern.findall(f) for f in fields]

your_ticket = list(map(int, data[1].split('\n')[1].split(',')))
nearby_tickets = [d.split(',') for d in data[2].split('\n')[1:]]

all_legal = set()
for field_row in fields:
    for field_range in field_row:
        mini, maxi = map(int, field_range.split('-'))
        numbers_in_range = list(range(mini, maxi+1))
        for num in numbers_in_range:
            all_legal.add(num)

sum_invalid = 0
new_rows = []
for nearby_row in nearby_tickets:
    new_row = []
    for nearby_num in map(int, nearby_row):
        if nearby_num not in all_legal:
            sum_invalid += nearby_num
        else:
            new_row.append(nearby_num)
    new_rows.append(new_row)

print(sum_invalid)

# Part B
row_ranges = []
for field_row in fields:
    row_range = set()
    for field_range in field_row:
        mini, maxi = map(int, field_range.split('-'))
        numbers_in_range = list(range(mini, maxi+1))
        for num in numbers_in_range:
            row_range.add(num)
    row_ranges.append(row_range)

mappings = {}
for position in range(len(row_ranges)):
    at_position = []
    for row in new_rows:
        if len(row) > position:
            at_position.append(row[position])
    for row_range_index in range(len(row_ranges)):
        if all(num in row_ranges[row_range_index] for num in at_position):
            if mappings.get(your_ticket[position]):
                mappings[your_ticket[position]] += [row_range_index]
            else:
                mappings[your_ticket[position]] = [row_range_index]

to_remove = set()
for i in range(1, len(row_ranges)+1):
    key, codomain = [(key, values) for key, values in mappings.items()
                     if len(values) == i][0]
    for rem in to_remove:
        codomain.remove(rem)
    to_remove.add(codomain[0])
    mappings[key] = codomain

print(prod(key for key, values in mappings.items() if values[0] < 6))
