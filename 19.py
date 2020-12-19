import re
from typing import List

with open(f'inputs/19.txt') as f:
    rs, data = f.read().split('\n\n')

rules = {
    r.split(':')[0]: [
        s.lstrip().replace('"', '').split(' ')
        for s in r.split(':')[1].split(' | ')
    ]
    for r in rs.splitlines()
}

def find_patterns(start: int) -> List[str]:
    patterns = rules[str(start)]
    i = 0
    while i < len(patterns):
        j = 0
        while j < len(patterns[i]):
            el = patterns[i][j]
            if not el.isnumeric():
                j += 1
                continue
            row = patterns[i][:]
            for z, mapped in enumerate(rules[el]):
                if z == 0:
                    patterns[i][j] = mapped[0]
                    for k, inserted in enumerate(mapped[1:]):
                        patterns[i].insert(j + k + 1, inserted)
                else:
                    copy_row = row[:]
                    copy_row[j] = mapped[0]
                    for k, inserted in enumerate(mapped[1:]):
                        copy_row.insert(j+k+1, inserted)
                    patterns.append(copy_row)
        i += 1
    return [''.join(r) for r in patterns]


patterns_42 = find_patterns(42)
patterns_31 = find_patterns(31)

options_42 = '|'.join(patterns_42)
options_31 = '|'.join(patterns_31)

# Part A
no_loop_pattern = re.compile(f'({options_42}){{2}}({options_31})')
print(len([1 for line in data.splitlines() if no_loop_pattern.fullmatch(line)]))

# Part B
length_42 = len(patterns_42[0])
loop_pattern = re.compile(f'({options_42})+({options_31})+')
re_31 = re.compile(options_31)

res = 0
for line in data.splitlines():
    if loop_pattern.fullmatch(line):
        how_many_42 = 0
        while line[:length_42] in patterns_42:
            line = line[length_42:]
            how_many_42 += 1
        how_many_31 = len(re_31.findall(line))
        if how_many_42 > how_many_31:
            res += 1
print(res)
