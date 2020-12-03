from numpy import product

tree_symbol = '#'

file = open('inputs/3.txt')
board = [line for line in file.read().split('\n')]
board_length = len(board[0])

def traverse(right: int, down: int) -> int:
    """
    Traverse the board until there are no more rows.

    Args:
        right: How many steps do we go to the right?
        down: How many steps do we go down?

    Returns:
        The number of trees encountered.
    """
    x = 0
    y = 0
    trees = 0

    while True:
        try:
            position = board[y + down][(x + right) % board_length]
            x += right
            y += down
            if position == tree_symbol:
                trees += 1
        except IndexError:
            break

    return trees


# Part A - O(n)
print(traverse(3, 1))

# Part B - O(n)
print(product([
    traverse(1, 1), traverse(3, 1), traverse(5, 1),
    traverse(7, 1), traverse(1, 2)
]))
