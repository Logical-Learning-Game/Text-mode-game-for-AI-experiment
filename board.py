"""
. - Empty Tile
x - Blocked Tile
* - 1 score Tile
P - Player Character
G - Goal Tile
"""

from action import Action
import copy
import util

EMPTY = "."
BLOCK = "x"
SCORE = "*"
PLAYER = "P"
GOAL = "G"

TILE_IDX = {
    PLAYER: 0,
    SCORE: 1,
    GOAL: 2
}

class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"


class Board:
    def __init__(self, board: list[str], player_position: Position, score: int, remaining_score: int):
        self.board = board
        self.player_position = player_position
        self.score = score
        self.remaining_score = remaining_score
        self.zobrist_table = util.generate_zobrist_table(board)
    
    @classmethod
    def from_string(cls, s: str):
        s = s.lstrip()
        s = s.rstrip()
        lst = s.split("\n")

        for i in range(len(lst)):
            lst[i] = lst[i].lstrip()
            lst[i] = lst[i].rstrip()
            lst[i] = list(lst[i])

        player_pos = None
        remaining_score = 0
        for i, row in enumerate(lst):
            for j, tile in enumerate(row):
                if tile == PLAYER:
                    player_pos  = Position(j, i)
                elif tile == SCORE:
                    remaining_score += 1

        return cls(lst, player_pos, 0, remaining_score)

    def update(self, action: str):
        x, y = self.player_position.x, self.player_position.y
        to_move = None

        new_board = copy.deepcopy(self)

        if action == Action.UP:
            new_board.player_position.y -= 1
            to_move = (x, y - 1)
        elif action == Action.DOWN:
            new_board.player_position.y += 1
            to_move = (x, y + 1)
        elif action == Action.LEFT:
            new_board.player_position.x -= 1
            to_move = (x - 1, y)
        elif action == Action.RIGHT:
            new_board.player_position.x += 1
            to_move = (x + 1, y)

        if to_move:
            new_board.board[y][x] = EMPTY
            if new_board.board[to_move[1]][to_move[0]] == SCORE:
                new_board.score += 1
                new_board.remaining_score -= 1
            new_board.board[to_move[1]][to_move[0]] = PLAYER

        return new_board

    def is_goal_state(self):
        for row in self.board:
            for tile in row:
                if tile == GOAL:
                    return False
        return self.remaining_score == 0

    def check_passable_tile(self, x: int, y: int):
        if y < 0 or  x < 0 or y > len(self.board) - 1 or x > len(self.board[y]) - 1:
            return False
        
        if self.remaining_score == 0:
            return self.board[y][x] in {EMPTY, SCORE, GOAL}
        
        return self.board[y][x] in {EMPTY, SCORE}


    def get_valid_actions(self):
        x, y = self.player_position.x, self.player_position.y
        
        if self.check_passable_tile(x, y - 1):
            yield Action.UP

        if self.check_passable_tile(x, y + 1):
            yield Action.DOWN

        if self.check_passable_tile(x - 1, y):
            yield Action.LEFT

        if self.check_passable_tile(x + 1, y):
            yield Action.RIGHT

    def __hash__(self):
        hash_value = 0
        table = self.zobrist_table

        idx = 0
        for i, row in enumerate(self.board):
            for j, tile in enumerate(row):
                if tile not in {EMPTY, BLOCK}:
                    tile_zobrist_idx = TILE_IDX[tile]
                    hash_value ^= table[idx][tile_zobrist_idx]
                idx += 1

        return hash_value

    def __eq__(self, other):
        if isinstance(other, Board):
            return hash(self) == hash(other)
        return False

    def __str__(self):
        s = ""
        for row in self.board:
            for tile in row:
                s += tile
            s += "\n"
        return s