from PawnLogic import Board
from unit_test import *


class Minimax(Board):
    def minimax(self, board_state, a, b):
        turn, board = board_state
        if super().utility_statics(board_state):
            return super().utility_statics(board_state)
        else:
            if turn == -1:
                value = 250
                for x in super().successor_generator(board_state):
                    value = min(value, self.minimax(x, a, b))
                    b = min(b, value)
                    if b <= a:
                        break
            elif turn == 1:
                value = -250
                for x in super().successor_generator(board_state):
                    value = max(value, self.minimax(x, a, b))
                    a = max(a, value)
                    if b <= a:
                        break
        result = board_state, value
        return value

    def decision_maker(self, board_state):
        compare = {1: max, -1: min}
        last_generation = super().successor_generator(board_state)
        # last_generation creates three successors e.g. [10, max] [9,max] [8,max]
        last_generation_utilies = [self.minimax(x, -250, 250) for x in last_generation]
        # last_generation utilites basically estimates utility values for each successor.
        combined = list(zip(last_generation, last_generation_utilies))
        # e.g. [(10, max), 100] [(9, max), 100] [(8, max), -100]
        best_selector = compare[board_state[0]]
        # best_selector call
        # s function from dictionary. E.g. for above situation, it calls object 'min' from (11, min)
        result = best_selector(combined, key=lambda item: item[1])
        # Since best_successor called the function to make decision of minimum values of array, it finds minimum value
        # E.g. [(10, max), 100] [(9, max), 100] [(8, max), -100] = [(8, max), -100]
        return (result)

if __name__ == '__main__':
    unit_testing().test_moves()
    unit_testing().winning_positions()
    initial_state = (-1, [[0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0],
                        [0, -1, 0, 0, 0, 0],
                        [-1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0]])
    new_board = Minimax()
    new_board.decision_maker(initial_state)
