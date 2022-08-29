import random

PIECES = 3

def generate_zobrist_table(board: list[list[str]]):
    size = 0
    for row in board:
        for tile in row:
            size += 1

    table = [[0 for _ in range(PIECES)] for _ in range(size)]

    for i in range(size):
        for j in range(PIECES):
            table[i][j] = random.getrandbits(64)

    return table