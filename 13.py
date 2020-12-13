from typing import Tuple, List
import math

with open('inputs/13.txt') as f:
    data = f.read().split('\n')

time = int(data[0])
bus_times = [int(time) for time in data[1].split(',') if time != 'x']

# Part A
smallest_multiples = []
multiple = 1
for num in bus_times:
    while num * multiple < time:
        multiple += 1
    smallest_multiples.append((num * multiple - time, num))
    multiple = 1

print(math.prod(min(smallest_multiples, key=lambda x: x[0])))


# Part B
def extended_euclidean(a: int, b: int) -> Tuple[int, int, int]:
    """Return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    if a == 0:
        return b, 0, 1
    else:
        b_div_a, b_mod_a = divmod(b, a)
        g, x, y = extended_euclidean(b_mod_a, a)
        return g, y - b_div_a * x, x

def modular_inverse(a: int, b: int) -> int:
    """return x such that (x * a) % b == 1"""
    g, x, _ = extended_euclidean(a, b)
    return x % b


def chinese_remainder_theorem(moduli: List[int], x: List[int]) -> int:
    while len(x) != 1:
        new_x = sum([
            modular_inverse(moduli[1], moduli[0]) * x[0] * moduli[1],
            modular_inverse(moduli[0], moduli[1]) * x[1] * moduli[0]
        ])
        new_modulus = moduli[0] * moduli[1]

        x = x[2:]
        x = [new_x % new_modulus] + x

        moduli = moduli[2:]
        moduli = [new_modulus] + moduli

    return x[0]


offsets = [-1*i for i, t in enumerate(data[1].split(',')) if t != 'x']
print(chinese_remainder_theorem(bus_times, offsets))
