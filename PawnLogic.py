import random
import numpy as np
import copy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from math import sqrt

'''Board class for the game of Pawn Game.
Default board size is 6x6.
Board data:
  1=white, -1=black, 0=empty
  first dim is column , 2nd is row:
     pieces[0][0] is the top left square,
     pieces[5][0] is the bottom left square,
     
Squares are stored and manipulated as (x,y) tuples.

Author: Vural Erdogan, github.com/vuralerdoganai
Date: March 6, 2019.

'''

class Board(): # includes board rules and successor creator

    def __init__(self, n = (4, 4), default_team = None, turn = None): # visualise all the successors if you choose none
        self.x = n[0]
        self.y = n[1]
        self.default_team = default_team
        self.turn = turn
        # Create the initial board array.
        self.pieces = [None] * self.x
        for i in range(self.x):
            self.pieces[i] = [0] * self.y
        self.pieces[0]=[1] * self.y # First team default position
        self.pieces[-1]=[-1] * self.y #second team default position


    def __getitem__(self, index):
        return self.pieces[index]

    def create_random_index(self, team_color):  # add [][] indexer syntax to the Board
        x = random.randint(1, self.x - 2)
        y = random.randint(0, self.y - 1)
        self.pieces[x][y] = team_color

    def random_board(self): # random board state creater without 'turn'
        for i in range(self.x):
            self.pieces[i]=[0]*self.y

        random_piece_number = self.x # create maksimum 12 pieces. Max 6 for each team.
        for i in range(random_piece_number):
            self.create_random_index(1)
            self.create_random_index(-1)

        fig2 = plt.figure(figsize=(3, 3))
        plt.imshow(self.pieces, interpolation='nearest')

    def get_pawn_positions(self): # help to get pawn positions with the team colour '-1' or '1'
        pawn_position_list = set()
        for y in range(self.y):
            for x in range(self.x):
                if not self.pieces[x][y] == 0:
                    pawn_position_list.add((self.pieces[x][y],(x, y)))
        return list(pawn_position_list)

    def get_cordinates(self, active_pawn): # Active Pawn represents next possible state of a pawn.
        x, y = active_pawn[1]
        return x, y

    def check_empty(self, active_pawn): # check the enemy pawn if it is empty or not to move forward
        all_pawn_positions = self.get_pawn_positions()
        for pawn in all_pawn_positions:
            if active_pawn[1] == pawn[1] :
                return False
        return True

    def convert_board_state(self, board_state):
        turn, state = board_state
        assert self.default_team == -1, "Vural we've got a problem"
        new_board_state = np.array([np.array(xi) * -1 for xi in state])
        turn, board = -turn, new_board_state
        board = np.flipud(board)
        board = [list(x) for x in board]
        new_board_state = (turn, board)
        return new_board_state

    def get_board_coppy(self): # help to copy the initial board position.
        coppy_board = copy.deepcopy(self.pieces)
        return coppy_board

    def move_executor(self, action_tuple): # execute the move from St1 to St2.
        position1, position2 = self.get_positions_from_action_tuple(action_tuple)
        position_1_cord_x, position_1_cord_y = self.get_cordinates(position1)
        position_2_cord_x, position_2_cord_y = self.get_cordinates(position2)
        new_board = self.get_board_coppy()
        if isinstance(new_board[1], tuple):
            new_board = [list(x) for x in new_board]
        new_board[position_1_cord_x][position_1_cord_y] = 0 # delete old position
        new_board[position_2_cord_x][position_2_cord_y] = position2[0]
        return new_board

    def get_enemy_pawn(self, reference_pawn): # diagonal move
        all_pawn_positions = self.get_pawn_positions()
        new_successor=[]
        for target_pawn in all_pawn_positions: # target_pawn includes team colour and pawn cordinates. (1, (3, 4)).
            target_pawn_team, target_pawn_cordinates = target_pawn
            reference_pawn_team, reference_pawn_cordinates = reference_pawn
            diagonal_difference = np.subtract(reference_pawn_cordinates, target_pawn_cordinates)
            # e.g. (1, (3, 4)) vs (-1, (4, 5)). Team colour also helps us to realise this equation.
            if (-target_pawn_team == reference_pawn_team) and (diagonal_difference[0] == -1*reference_pawn_team) and(abs(diagonal_difference[1]) == 1):
                new_pawn_position = (-target_pawn_team,) + target_pawn[1:]
                executed_board_position = self.move_executor((reference_pawn, new_pawn_position))
                new_successor.append((-reference_pawn_team, executed_board_position))
                continue
        if new_successor == None:
            return False
        return new_successor

    def extract_legal_moves_considering_team(self, created_move_list, team = None):
        if team:
            created_move_list = [x for x in created_move_list if x[0] == -team]
        return created_move_list

    def successor_generator(self, *input_state):
        for state in input_state:    # this input state is optional to start from any board state.
            self.board_position_assigner(state)
        legal_moves=[]
        all_pawn_positions = self.get_pawn_positions()

        #First move creator (forward)
        for active_pawn in all_pawn_positions:
            target_location = (active_pawn[0], ((active_pawn[1][0]+active_pawn[0]),) + active_pawn[1][1:])
            try:
                assert self.check_empty(target_location)
                # legal_moves.append((x, move1))
                new_successor = self.move_executor((active_pawn, target_location))
                legal_moves.append((-active_pawn[0], new_successor))
            except AssertionError as error:
                continue
        #Second move creator (diagonal)
        for active_pawn in all_pawn_positions:
            try:
                assert self.get_enemy_pawn(active_pawn)
                target_pawn = self.get_enemy_pawn(active_pawn)
                legal_moves.extend(target_pawn)
            except AssertionError as error:
                continue
        extracted_legal_moves = self.extract_legal_moves_considering_team(legal_moves, self.turn)
        random.shuffle(extracted_legal_moves)
        return extracted_legal_moves

    def board_position_assigner(self, state): # assign any board position and team as initial state.
        self.turn = state[0]
        self.pieces[:]= state[1]

    def random_move(self, list_moves): # random move creator from pawn position.
        random_move = random.randint(0, len(list_moves) - 1)
        return list_moves[random_move]

    def find_winner(self, board_state):
        if self.terminal_state(board_state):
            value = self.heuristic_value(board_state)
            return True if value > 0 else False
        else:
            return None

    def hash_converter(self, board_state):
        nested_lst_of_tuples = [tuple(l) for l in board_state]
        return tuple(nested_lst_of_tuples)

    def terminal_state(self, board_state, depth=None): # winning positions
        if depth == 0:
            return True
        turn, board = board_state[0], board_state[1]
        if -1 in board[0] or 1 in board[-1]:   # check the last rows if there is pawn or not. We are yellow as default.
            return True     #turn will be always "1"
        created_moves = self.successor_generator(board_state)
        if not created_moves: # no moves due to no pawn or pawn stacks
            return True
        else:
            return False

    def heuristic_value(self, board_state, depth=5e103):
        assert self.terminal_state(board_state, depth) # manhattan distance has been used for heuristic.
        turn, board = board_state[0], board_state[1]
        if -1 in board[0]:  # check the last rows if there is pawn or not. We are yellow as default.
            return -(100+depth*0.001)  # turn will be always "1"
        if 1 in board[-1]:
            return 100+depth*0.001  # turn will be alway "-1"
        created_moves = self.successor_generator(board_state)
        if not created_moves:  # no moves due to no pawn or pawn stacks
            return (-(100+depth*0.001))*turn
        if depth is not 5e103:
            self.board_position_assigner(board_state)
            pawn_positions_list = self.get_pawn_positions()
            yellow_team = []
            purple_team = []
            board_size_x, board_size_y = np.asarray(board).shape
            promotion_value = 0
            for pawn in pawn_positions_list:
                if 1 == pawn[0]: # team colour is pawn[0]
                    promotion_value += pawn[1][0] - (len(board)-1)
                    yellow_team.append(pawn)
                elif -1 == pawn[0]:
                    promotion_value +=  pawn[1][0]
                    purple_team.append(pawn)
                else:
                    raise Exception('pawn list has some values different from team values.')

            pawn_number_difference_value = (len(yellow_team) - len(purple_team) + 1)* abs(len(yellow_team)-len(purple_team))

            cols = [None] * len(board)
            distance_score = 0
            for row in board:
                for j, col in enumerate(row):
                    if cols[j] is None:
                        if col == turn:
                            cols[j] = 0
                    elif col == -turn:
                        distance_score += cols[j]
                    else:
                        cols[j] += 1

            distance_score = ((-1)**(distance_score+1))*distance_score

            utility_value = promotion_value + 2*pawn_number_difference_value + distance_score

            return (utility_value)*turn


    def get_positions_from_action_tuple(self, positions):
        first_position = positions[0]
        second_position = positions[1]
        return first_position, second_position

if __name__ == '__main__':
        new_board = Board(default_team = 1, turn = 1, n=(5,5))
        new_board.random_board()
        successor_list = new_board.successor_generator()
        print('successors:', list(successor_list), len(successor_list))
        fig=plt.figure(figsize=(8, 5))
        row = int(sqrt(len(successor_list))) + 1
        column = int(sqrt(len(successor_list))) +1
        print(row, column)
        for i in range(1, len(successor_list)+1):
            img = successor_list[i-1][1]
            fig.add_subplot(row, column, i)
            plt.imshow(img)
        plt.show()
        # z = x.random_move(y, 1)
        # x.move_executor(z)
        # z = x.random_move(y, 1)
        # x.move_executor(z)
        # print(z)


