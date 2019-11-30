import random
from minimax import Minimax
from PawnLogic import Board
import numpy as np
from MCTSplayer import PawnBoardState
from MCTS import MCTS

class Player:

    def minimax_player(self, state, depth=2500000, team = 1, heuristic_parameter=True):  # creates first successors to implement minimax algorithm
        new_shape_x = np.asarray(state[1]).shape
        player1 = Minimax(n = new_shape_x, default_team = team, advance_option = heuristic_parameter)
        print('default_team', team, player1.default_team)
        if team == -1:
            state = player1.convert_board_state(state)
        best_move = player1.decision_maker(state, depth)
        chosen_succ, utility = best_move
        if team == -1:
            chosen_succ = player1.convert_board_state(chosen_succ)
        return chosen_succ

    def random_player(self, state):  # choose random state from successors.
        new_shape_x = np.asarray(state[1]).shape
        player2 = Board(n=new_shape_x)
        succ_list = player2.successor_generator(state)
        random_move = random.randint(0, len(succ_list) - 1)
        return succ_list[random_move]

    def human_player(self, state):
        new_shape_x = np.asarray(state[1]).shape
        player3 = Board(n=new_shape_x)
        succ_list = player3.successor_generator(state)
        print('Current State is:', state)
        for x, elem in enumerate(succ_list):
            print('{0}:{1}'.format(x, elem[1]))
        player_move = int(input('Choose your move number:'))
        return succ_list[player_move]

    def mcts_player(self, state, roll_out = 1, team = 1):
        new_shape_x = np.asarray(state[1]).shape
        player4 = Board(n=new_shape_x, default_team = team)
        if team == -1:
             state = player4.convert_board_state(state)
        turnx, board = state
        board = [tuple(l) for l in board]
        state = PawnBoardState(turnx, tuple(board), winner = None, terminal = False)
        tree = MCTS()
        for _ in range(roll_out):
            tree.do_rollout(state)
        state = tree.choose(state)
        turnx, board = state[0], state[1]
        new_board = [list(l) for l in board]
        new_state = [turnx, new_board]
        if team == -1:
            new_state = player4.convert_board_state(new_state)
        return new_state

