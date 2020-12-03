from numpy import product

tree_symbol = '#'

file = open('inputs/3.txt')
board = file.read().split('\n')
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
    x = y = trees = 0

    while True:
        try:
            x += right
            y += down
            position = board[y][x % board_length]
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
