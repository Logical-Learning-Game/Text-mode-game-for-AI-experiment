
"""
. - Empty Tile
x - Blocked Tile
* - 1 score Tile
P - Player Character
F - Finish Tile
"""

board = """
        ....*..xx
        .x.x.x.xx
        ..*...*..
        .x.x.x.x.
        P.......F
        """

def boardstr_to_boardlist(boardstr: str):
    boardstr = boardstr.lstrip()
    boardstr = boardstr.rstrip()
    lst = boardstr.split("\n")

    for i in range(len(lst)):
        lst[i] = lst[i].lstrip()
        lst[i] = lst[i].rstrip()
    
    return lst


if __name__ == "__main__":
    board = boardstr_to_boardlist(board)

