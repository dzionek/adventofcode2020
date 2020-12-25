with open('inputs/25.txt') as f:
    data = f.read().splitlines()

card_public_key = int(data[0])
door_public_key = int(data[1])


def find_loop_size(stop: int):
    sub = 7
    val = 1
    loop_size = 0
    while val != stop:
        val *= sub
        val %= 20201227
        loop_size += 1
    return loop_size


def transform(sub: int, loop_size: int):
    val = 1
    for _ in range(loop_size):
        val *= sub
        val %= 20201227
    return val


card_loop_size = find_loop_size(card_public_key)
door_loop_size = find_loop_size(door_public_key)
print(transform(card_public_key, door_loop_size))
