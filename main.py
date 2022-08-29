from board import Board
from agent.search import uniform_cost_search


board_str = """
        ....*..xx
        .x.x.x.xx
        ..*...*..
        .x.x.x.x.
        P.......G
        """

board_str2 = """
        .*.xxxxxx
        .x.xxxxG.
        ...xx.xx.
        x.xxx*xx*
        x........
        xxxxx.xxx
        xxP...xxx
        """

if __name__ == "__main__":
    board = Board.from_string(board_str)

    result = uniform_cost_search(board)
    print(result)

