from typing import List
import re
from itertools import product

with open('inputs/14.txt') as f:
    data = f.read().split('\n')

# Part A
memory = {}
mask = ""

for line in data:
    first, second = line.split(' = ')
    if first == 'mask':
        mask = second
    else:
        address = int(''.join([c for c in first if c.isnumeric()]))
        bin_string = "{0:b}".format(int(second))
        bin_string = (len(mask) - len(bin_string)) * '0' + bin_string
        res = 0
        for i in range(1, len(mask)+1):
            if mask[-1 * i] != 'X':
                res += 2**(i-1) * int(mask[-1 * i])
            else:
                res += 2**(i-1) * int(bin_string[-1 * i])
        memory[address] = res

print(sum(memory.values()))

# Part B
def find_masks(mask: str) -> List[str]:
    floating_positions = [m.start() for m in re.finditer('X', mask)]
    options = list(product(['0', '1'], repeat=len(floating_positions)))
    masks = [[c for c in mask]] * len(options)
    for i in range(len(options)):
        mask = masks[i][:]
        for j, replacement in zip(floating_positions, options[i]):
            mask[j] = replacement
        masks[i] = mask[:]

    return [''.join(m) for m in masks]


memory = {}
mask = None

for line in data:
    first, second = line.split(' = ')
    if first == 'mask':
        mask = second
    else:
        address = int(''.join([c for c in first if c.isnumeric()]))
        address_mask = "{0:b}".format(int(address))
        address_mask = (len(mask) - len(address_mask)) * '0' + address_mask
        address_mask = [c for c in address_mask]
        for i in range(1, len(mask)+1):
            if mask[-1 * i] in '1X':
                address_mask[-1 * i] = mask[-1 * i]
        address_mask = ''.join(address_mask)

        for real_address in find_masks(address_mask):
            real_address = int(real_address, 2)
            memory[real_address] = int(second)

print(sum(memory.values()))
