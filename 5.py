from math import floor, ceil

file = open('inputs/5.txt')
data = file.read().split('\n')

last_row = 127
last_col = 7

def find_seat(line: str, row: bool = False) -> str:
    """
    Find the position of a row or column.

    Args:
        line: The boarding pass.
        row: True if we want to get a row, False for column.

    Returns:
        The row or column of a seat.

    """
    letters = line[:7] if row else line[7:]
    start, end = 0, last_row if row else last_col

    for letter in letters:
        if letter in 'BR':
            start, end = start + ceil((end - start) / 2), end
        else:
            start, end = start, start + floor((end - start) / 2)

    return start


# Part A - O(n lg n)
seats = [
    int(8 * find_seat(line, row=True) + find_seat(line))
    for line in data
]
seats.sort(reverse=True)

print(seats[0])

# Part B - O(n)
last_seat = seats[0]
for seat in seats[1:]:
    if seat != last_seat - 1:
        break
    last_seat = seat

print(last_seat - 1)
