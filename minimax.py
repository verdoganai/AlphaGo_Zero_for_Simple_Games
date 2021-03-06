from PawnLogic import Board
from unit_test import *
import numpy as np

class Minimax(Board):

    def minimax(self, board_state, a, b, depth = None):
        turn, board = board_state
        if super().terminal_state(board_state, depth):
            return super().heuristic_value(board_state, depth)
        else:
            if turn == -1:
                value = 250
                for x in super().successor_generator(board_state):
                    if depth is not None:
                        value = min(value, self.minimax(x, a, b, depth - 1))
                    else:
                        value = min(value, self.minimax(x, a, b))
                    b = min(b, value)
                    if b <= a:
                        break
            elif turn == 1:
                value = -250
                for x in super().successor_generator(board_state):
                    if depth is not None:
                        value = max(value, self.minimax(x, a, b, depth - 1))
                    else:
                        value = max(value, self.minimax(x, a, b))
                    a = max(a, value)
                    if b <= a:
                        break
        result = board_state, value
        return value

    def decision_maker(self, board_state, depth = 4):
        compare = {1: max, -1: min}
        a, b = -250, 250
        last_generation = super().successor_generator(board_state)
        last_generation_utilies = [self.minimax(x, a, b, depth) for x in last_generation]
        print(last_generation_utilies)
        combined = list(zip(last_generation, last_generation_utilies))
        best_selector = compare[board_state[0]]
        result = best_selector(combined, key=lambda item: item[1])
        return (result)



if __name__ == '__main__':
    unit_testing().test_moves()
    unit_testing().winning_positions()
    initial_state = (-1, [[0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 1, -1, 0],
                         [0, 1, 1, 0, 0, 0],
                         [1, -1, 0, 0, -1, -1],
                         [0, 0, 0, 1, 0, 0],
                         [0, 0, 0, 0, 0, 0]])

    initial_state2 = (1, [[ 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 1, -1, 0],
                          [0, 1, 1, 0, 0, 0],
                          [1, -1, 0, 0, -1, -1],
                          [ 0, 0, 1, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0]])
    initial_state4 = (1, [[1, 1, 1, 1, 1, 1],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [-1, -1, -1, -1, -1, -1]])

    initial_state3 =  (1, [[1, 1, 0, 1],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, -1, -1, -1]])

    new_shape_x = np.asarray(initial_state4[1]).shape
    new_board = Minimax(n = new_shape_x, default_team=1)
    new_board.decision_maker(initial_state4) # depth is optional
