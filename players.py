import random
from minimax import Minimax
from PawnLogic import Board

class Player:

    def minimax_ai_player(self, state):  # creates first successors to implement minimax algorithm.

        player1 = Minimax()
        best_move = player1.decision_maker(state)
        chosen_succ, utility = best_move
        return (chosen_succ)

    def random_player(self, state):  # choose random state from successors.
        player2 = Board()
        succ_list = player2.successors_generator(state)
        random_move = random.randint(0, len(succ_list) - 1)
        return succ_list[random_move]

    def human_player(self, state):
        player3 = Board()
        succ_list = player3.successors_generator(state)
        print('Current State is:', state)
        for x, elem in enumerate(succ_list):
            print('{0}:{1}'.format(x, elem[1]))
        player_move = int(input('Choose your move number:'))
        return succ_list[player_move]

