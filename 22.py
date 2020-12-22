from collections import deque
from typing import Deque

with open('inputs/22.txt') as f:
    data = f.read().split('\n\n')

first_player_initial = deque(map(int, data[0].splitlines()[1:]))
second_player_initial = deque(map(int, data[1].splitlines()[1:]))


def get_score(winner_cards: Deque[int]) -> int:
    return sum([
        i * winner_cards.popleft()
        for i in reversed(range(1, len(winner_cards) + 1))
    ])


# Part A
def play_game_a(first_player: Deque[int], second_player: Deque[int]) -> bool:
    """Return True if the first player won a game."""
    while first_player and second_player:
        first_card = first_player.popleft()
        second_card = second_player.popleft()
        if first_card > second_card:
            first_player.append(first_card)
            first_player.append(second_card)
        else:
            second_player.append(second_card)
            second_player.append(first_card)

    return True if len(first_player) != 0 else False


first, second = first_player_initial.copy(), second_player_initial.copy()
print(get_score(first if play_game_a(first, second) else second))

# Part B
def play_game_b(first_player: Deque[int], second_player: Deque[int]) -> bool:
    """Return True if the first player won a game."""
    history = set()
    while first_player and second_player:
        order = (tuple(first_player), tuple(second_player))
        if order in history:
            return True

        history.add(order)

        first_card = first_player.popleft()
        second_card = second_player.popleft()

        if first_card <= len(first_player) and second_card <= len(second_player):
            copied_first = first_player.copy()
            copied_second = second_player.copy()
            while len(copied_first) != first_card:
                copied_first.pop()
            while len(copied_second) != second_card:
                copied_second.pop()

            if play_game_b(copied_first, copied_second):
                first_player.append(first_card)
                first_player.append(second_card)
            else:
                second_player.append(second_card)
                second_player.append(first_card)
        else:
            if first_card > second_card:
                first_player.append(first_card)
                first_player.append(second_card)
            else:
                second_player.append(second_card)
                second_player.append(first_card)

    return True if len(first_player) != 0 else False


first, second = first_player_initial.copy(), second_player_initial.copy()
print(get_score(first if play_game_b(first, second) else second))
