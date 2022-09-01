from board import Board
import heapq


class ProblemState:
    def __init__(self, board: Board, action: str = None, prev_state = None):
        self.board = board
        self.action = action
        self.prev_state = prev_state
        self.cost = self.calculate_cost()

    def calculate_cost(self):
        if not self.prev_state:
            return 0

        to_add_cost = 1
        if self.board.status == "slow":
            to_add_cost = 2

        cost = self.prev_state.cost + to_add_cost

        return cost

    def __hash__(self):
        return self.board.__hash__()

    def __eq__(self, other):
        return self.board.__eq__(other.board)

    # define for min heap
    def __lt__(self, other):
        return self.cost < other.cost


def solution(state: ProblemState):
    result = []
    while state.action:
        result.append(state.action)
        state = state.prev_state

    return list(reversed(result))


def find_priority_queue(priority_queue: list[ProblemState], state: ProblemState):
    for s in priority_queue:
        if s == state:
            return s
    return None


def uniform_cost_search(board: Board):
    initial_state = ProblemState(board)

    priority_queue = [initial_state]
    heapq.heapify(priority_queue)

    explored_set = set()

    while len(priority_queue) > 0:
        state = heapq.heappop(priority_queue)

        if state.board.is_goal_state():
           return solution(state), state.cost

        explored_set.add(state)

        for action in state.board.get_valid_actions():
            updated_board = state.board.update(action)

            child_state = ProblemState(updated_board, action, prev_state=state)

            if child_state not in explored_set and child_state not in priority_queue:
                heapq.heappush(priority_queue, child_state)
            else: 
                s = find_priority_queue(priority_queue, child_state)

                if s and child_state.cost < s.cost:
                    idx = priority_queue.index(s)
                    priority_queue[idx] = child_state
                    heapq.heapify(priority_queue)

