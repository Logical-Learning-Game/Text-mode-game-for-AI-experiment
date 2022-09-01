import random


def generate_zobrist_table(board: list[list[str]], pieces_size: int):
    size = 0
    for row in board:
        for tile in row:
            size += 1

    table = [[0 for _ in range(pieces_size)] for _ in range(size)]

    for i in range(size):
        for j in range(pieces_size):
            table[i][j] = random.getrandbits(64)

    return table