import re
from typing import Optional, List, Tuple
from enum import Enum, auto

class Precedence(Enum):
    ADD = auto()
    MULT = auto()


with open('inputs/18.txt') as f:
    data = f.read().splitlines()


def count(expr: str, higher_precedence: Optional[Precedence] = Precedence.MULT,
          again: bool = False) -> int:
    while '(' in expr:
        parens = find_parens(expr)
        start, end, depth = min(parens, key=lambda x: x[2])
        expr = expr[:start] + str(
            count(expr[start+1:end], higher_precedence, again)
        ) + expr[end+1:]
    if higher_precedence:
        if not again:
            if higher_precedence == Precedence.ADD:
                expr = re.sub(r'(\d+( \+ \d+)+)', r'(\1)', expr)
            else:
                expr = re.sub(r'(\d+( \* \d+)+)', r'(\1)', expr)
            return count(expr, higher_precedence, True)
    expr_array = expr.split(' ')
    sub_res = int(expr_array[0])
    for i, ch in enumerate(expr_array[1:]):
        if i % 2 == 0:
            operator = ch
        else:
            if operator == '+':
                sub_res += int(ch)
            else:
                sub_res *= int(ch)
    return sub_res


def find_parens(expr: str) -> List[Tuple[int, int, int]]:
    parens = []
    stack = []

    for i, c in enumerate(expr):
        if c == '(':
            stack.append(i)
        elif c == ')':
            parens.append((stack.pop(), i, len(stack)))

    return parens


total_sum_equal = 0
total_sum_add_first = 0
for line in data:
    total_sum_equal += count(line, None)
    total_sum_add_first += count(line, Precedence.ADD)

print(f'{total_sum_equal}\n{total_sum_add_first}')
