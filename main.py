from minimax import Minimax
from PawnLogic import Board
from players import Player
from unit_test import *


if __name__ == '__main__':
    unit_testing().test_moves()
    unit_testing().winning_positions()
    initial_state = (-1, [[0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0],
                        [0, -1, 0, 0, 0, 0],
                        [-1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0]])
    game_player = Player()
    move = game_.minimax_ai_player(initial_state)
    print(move)
