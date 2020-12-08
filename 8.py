from typing import Tuple, List

with open('inputs/8.txt') as f:
    data = [
        (line.split(' ')[0], int(line.split(' ')[1]))
        for line in f.read().split('\n')
    ]

Instruction = Tuple[str, int]


class Program:
    def __init__(self, instructions: List[Instruction]) -> None:
        self.instructions = instructions
        self.acc = 0
        self.pc = 0
        self.visited = [False] * len(data)

    def next_line(self) -> None:
        instr = self.instructions[self.pc]
        self.visited[self.pc] = True

        if instr[0] == 'acc':
            self.acc += instr[1]
            self.pc += 1
        elif instr[0] == 'jmp':
            self.pc += instr[1]
        elif instr[0] == 'nop':
            self.pc += 1
        else:
            raise ValueError(f'Instruction {instr[0]} is not supported')

    def is_next_visited(self) -> bool:
        return self.visited[self.pc]

    def is_terminating(self) -> bool:
        return self.pc == len(data)


# Part A
def solve_first() -> None:
    program = Program(data)
    while not program.is_next_visited():
        program.next_line()
    print(program.acc)


# Part B
def solve_second() -> None:
    for i in range(len(data)):
        changed_instr = data[i][0]

        if changed_instr == 'nop':
            data[i] = ('jmp', data[i][1])
        elif changed_instr == 'jmp':
            data[i] = ('nop', data[i][1])
        else:
            continue

        program = Program(data)

        while not program.is_next_visited():
            program.next_line()
            if program.is_terminating():
                print(program.acc)
                exit()

        data[i] = (changed_instr, data[i][1])


if __name__ == '__main__':
    solve_first()
    solve_second()
