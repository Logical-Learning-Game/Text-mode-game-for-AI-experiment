from board import Board
from action import Action


board_str = """
        ....*..xx
        .x.x.x.xx
        ..*...*..
        .x.x.x.x.
        P.......G
        """

if __name__ == "__main__":
    board = Board.from_string(board_str)
    
    while not board.is_goal_state():
        print(board)
        s = input()
        action = Action.from_string(s)
        board.update(action)

