from board import Board
from agent.search import breadth_first_search, uniform_cost_search
import os
import msvcrt


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

board_str3 = """
		!..G
		!...
		!...
		P...
		"""

if __name__ == "__main__":
	board = Board.from_string(board_str2)

	actions, cost = uniform_cost_search(board)
	print(actions, cost)
	
	for action in actions:
		print(board)

		msvcrt.getch()
		os.system("cls")

		board = board.update(action)

	print(board)


