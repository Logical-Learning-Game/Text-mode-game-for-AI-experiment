"""
. - Empty Tile
x - Blocked Tile
* - 1 score Tile
P - Player Character
G - Goal Tile
"""

from action import Action

EMPTY = "."
BLOCK = "X"
SCORE = "*"
PLAYER = "P"
GOAL = "G"

class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"


class Board:
    def __init__(self, board: list[str], player_position: Position):
        self.board = board
        self.player_position = player_position
    
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
        for i, row in enumerate(lst):
            for j, tile in enumerate(row):
                if tile == PLAYER:
                    player_pos  = Position(j, i)

        return cls(lst, player_pos)

    def update(self, action: str):
        x, y = self.player_position.x, self.player_position.y
        if action == Action.UP:
            self.board[y][x] = EMPTY
            self.board[y - 1][x] = PLAYER
            self.player_position.y -= 1
        elif action == Action.DOWN:
            self.board[y][x] = EMPTY
            self.board[y + 1][x] = PLAYER
            self.player_position.y += 1
        elif action == Action.LEFT:
            self.board[y][x] = EMPTY
            self.board[y][x - 1] = PLAYER
            self.player_position.x -= 1
        elif action == Action.RIGHT:
            self.board[y][x] = EMPTY
            self.board[y][x + 1] = PLAYER
            self.player_position.x += 1

    def is_goal_state(self):
        for row in self.board:
            for tile in row:
                if tile == GOAL:
                    return False
        return True

    def check_passable_tile(self, x: int, y: int):
        if y < 0 or  x < 0 or y > len(self.board) - 1 or x > len(self.board[y]) - 1:
            return False
        
        return self.board[y][x] in {EMPTY, SCORE, GOAL}


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

    def __str__(self):
        s = ""
        for row in self.board:
            for tile in row:
                s += tile
            s += "\n"
        return s