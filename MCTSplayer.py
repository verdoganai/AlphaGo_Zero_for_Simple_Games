import random

from collections import defaultdict, namedtuple
import math
from PawnLogic import Board
import numpy as np
from unit_test import *
from random import choice
from MCTS import MCTS, Node

_PBS = namedtuple("PawnBoardState", "turnx state winner terminal")

class PawnBoardState(_PBS, Board):
    def __init__(self, turnx=None, state=None, winner=None, terminal = None):
        super(PawnBoardState, self).__init__()


    def find_children(board_state):
        if board_state.terminal:
            return set()
        print('successors:', {board_state.make_move(i) for i in range(len(super().successor_generator(board_state)))})
        return {
            board_state.make_move(i) for i in range(len(super().successor_generator(board_state)))
        }

    def find_random_child(board_state):
        if board_state.terminal:
            return None

        succ_list = super().successor_generator(board_state)
        if succ_list:
            random_move = random.randint(0, len(succ_list) - 1)
            return board_state.make_move(random_move)
        else:
            raise 'No Child'
            return None

    def is_terminal(board_state):
        return board_state.terminal

    def reward(board_state):

        value = super().find_winner(board_state)
        if value == True: return 1
        elif value == False: return 0
        elif value is None: return 0.5


    def make_move(board_state, index):
        state_list = super().successor_generator(board_state)
        selected_board = state_list[index]
        turnx, state = selected_board
        winner = super().find_winner(selected_board)
        is_terminal = super().terminal_state(selected_board)
        state = super().hash_converter(state)
        return PawnBoardState(turnx, state, winner, is_terminal)


def new_pawn_board(board_state, winner=None, terminal = False):
    turnx, state = board_state

    return PawnBoardState(turnx, state, winner, terminal)


def get_shape(board):
    n = np.asarray(board[1]).shape
    return n

if __name__ == "__main__":
    initial_state = (-1, [[0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0],
                          [0, 1, 1, 0, 0, 0],
                          [1, -1, 0, 0, -1, -1],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0]])
    terminal_state = (1, [[0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, -1, 0, 0, -1, -1],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0]])

    tree = MCTS()
    size_board = get_shape(initial_state)
    new_state = new_pawn_board(initial_state)
    while True:
        choose_index = int(input('choose_index:'))
        new_state = new_state.make_move(choose_index)
        if new_state.terminal:
            break
        print('new_state', new_state)
        for _ in range(50):
            tree.do_rollout(new_state)
        new_state = tree.choose(new_state)

        print(new_state)
        if new_state.terminal:
            break