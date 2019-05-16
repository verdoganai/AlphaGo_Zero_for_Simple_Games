from minimax import Minimax
from PawnLogic import Board
from players import Player
from unit_test import *

from timeit import default_timer as timer


def start_position():
    return (-1, [[0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, -1, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [-1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]])


def increase_score(state):  # increases winner's score as 2 for terminal position.
    global max_score, min_score
    turn, board = state
    if turn == -1:
        max_score += 1
    else:
        min_score += 1
    return max_score, min_score


def game_manager():
    while True:  # determines players by user.
        player_1 = int(input('Determine first player; Random(0), AI(1), Human(2) :'))
        player_2 = int(input('Determine second player; Random(0), AI(1), Human(2): '))
        if player_1 in range(0, 3) and player_2 in range(0, 3):  # checking inputs
            break
        else:
            print('Out of range. Please choose a player')

    game = Player()
    players = [game.random_player, game.minimax_ai_player, game.human_player]
    chosen_players = [players[player_1], players[player_2]]  # collecting chosen players to create a turn switcher.
    first_player, _ = chosen_players[0].__name__.split('_')
    second_player, _ = chosen_players[1].__name__.split('_')
    players_names = [first_player, second_player]  # collecting chosen players' names to illustrate whose turn.
    print(first_player + " vs " + second_player + " have been chosen.")
    return chosen_players, players_names


def export_data(duration, max_score, min_score):
    print('Score: {0} {1} duration: {2} second'.format(max_score, min_score, time_result))
    initial_state = start_position()  # we coppied starting position to export heap value.
    with open('Time Analysing.txt', 'a') as f:  # export results
        print(duration, max_score, min_score, initial_state[1], file=f)


if __name__ == '__main__':
    unit_testing().test_moves()
    unit_testing().winning_positions()
    chosen_players, players_names = game_manager()
    max_score, min_score = 0, 0
    state = start_position()
    start = timer()
    current_board = Board()
    move_counter, turn_switcher = (0, 0)  # move counter
    while (move_counter < 200):  # maximum move limit
        print('%d:' % (turn_switcher + 1) + players_names[turn_switcher] + " player's move:")
        move = chosen_players[turn_switcher](state)
        current_board.board_position_assigner(move)
        print(current_board.pieces)
        if current_board.terminal_state(move):  # checking whether terminal state or not
            max_score, min_score = increase_score(move)

        print(max_score, min_score)
        move_counter += 1
        turn_switcher = move_counter % 2  # switching turn
        turn, board_state = state
        if not move_counter >= 200:  # checking whether list and move count to finish game.
            print("Game Over.")
            if max_score > min_score:
                print('First player "%s" win.' % players_names[0])
            elif min_score > max_score:
                print('Second player "%s" win.' % players_names[1])
            break

    end = timer()
    time_result = end - start
    export_data(time_result, max_score, min_score)


