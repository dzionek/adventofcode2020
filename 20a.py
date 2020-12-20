import numpy as np
from common_20 import all_transformations, transform

with open('inputs/20.txt') as f:
    data = f.read().split('\n\n')

tiles = {
    int(tile.splitlines()[0].split(' ')[1].rstrip(':')):
        np.array([[c for c in sub_line] for sub_line in tile.splitlines()[1:]])
    for tile in data
}

def is_matching(a: np.ndarray, b: np.ndarray, side: str) -> bool:
    if side == 'r':
        return np.all(a[:, -1] == b[:, 0])
    elif side == 'd':
        return np.all(a[-1, :] == b[0, :])


size = int(np.sqrt(len(tiles.keys())))
for tile_id, tile in tiles.items():
    for (t1_a, t1_b) in all_transformations:
        grid_ids = np.empty((size, size), dtype=np.longlong)
        grid = np.empty((size, size), dtype=np.object)
        remaining_tiles = set(tiles.keys())
        remaining_tiles.remove(tile_id)
        x = y = 0
        grid[x, y] = transform(t1_a, t1_b, tile)
        grid_ids[x, y] = tile_id
        y = 1
        while True:
            other_found = False
            for other_id in remaining_tiles:
                for (t2_a, t2_b) in all_transformations:
                    other_tile = transform(t2_a, t2_b, tiles[other_id])
                    match = True
                    if y != 0 and x == 0:
                        match = match and is_matching(grid[x, y-1], other_tile, 'r')
                    if x != 0:
                        match = match and is_matching(grid[x-1, y], other_tile, 'd')
                    if match:
                        other_found = True
                        grid[x, y] = other_tile
                        grid_ids[x, y] = other_id
                        y += 1
                        if y == size:
                            y = 0
                            x += 1
                        remaining_tiles.remove(other_id)
                        break
                if other_found:
                    break
            if not other_found:
                break
            if len(remaining_tiles) == 0:
                print(grid_ids[0, 0] * grid_ids[0, -1] * grid_ids[-1, 0] * grid_ids[-1, -1])
                with open('inputs/20_b.txt', 'w') as f:
                    text_to_write = ""
                    for grid_line in grid:
                        for line_in_square in range(len(tile)):
                            line = ""
                            for square_in_grid_line in range(size):
                                line += ''.join(
                                    grid_line[square_in_grid_line][line_in_square]
                                ) + ' '
                            line = line[:-1]
                            line += '\n'
                            text_to_write += line
                        text_to_write += '\n'
                    text_to_write = text_to_write[:-2]
                    f.write(text_to_write)
                exit()
