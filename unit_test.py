import unittest
from PawnLogic import Board


class unit_testing(unittest.TestCase):

    def test_moves(self):
        test_board = Board()
        teams = {'Purple': -1,
                 'Yellow': 1}

        reference_board_state = ([[0, 0, 0, 0, 0, 0],
                                [0, 0, 1, 1, 1, 0],
                                [0, -1, -1, -1, 0, 1],
                                [1, -1, 0, 0, 0, 0],
                                [-1, -1, 0, 1, 0, -1],
                                [0, 0, 0, 0, 0, 0]])

        compare_yellow_team = (teams['Yellow'], reference_board_state)
        test_board.board_position_assigner(compare_yellow_team)
        yellow_successor_list = test_board.successor_generator()

        test_yellow_team_successors = [(-1, [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, -1, -1, -1, 0, 1], [1, -1, 0, 0, 0, 0], [-1, -1, 0, 0, 0, -1], [0, 0, 0, 1, 0, 0]]),
                                       (-1, [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, -1, -1, -1, 0, 0], [1, -1, 0, 0, 0, 1], [-1, -1, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0]]),
                                       (-1, [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, -1, -1, -1, 1, 1], [1, -1, 0, 0, 0, 0], [-1, -1, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0]]),
                                       (-1, [[0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0], [0, -1, 1, -1, 0, 1], [1, -1, 0, 0, 0, 0], [-1, -1, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0]]),
                                       (-1, [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, -1, -1, 1, 0, 1], [1, -1, 0, 0, 0, 0], [-1, -1, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0]]),
                                       (-1, [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, -1, -1, -1, 0, 1], [0, -1, 0, 0, 0, 0], [-1, 1, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0]]),
                                       (-1, [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 1, -1, -1, 0, 1], [1, -1, 0, 0, 0, 0], [-1, -1, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0]]),
                                       (-1, [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, -1, -1, 1, 0, 1], [1, -1, 0, 0, 0, 0], [-1, -1, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0]])]

        self.assertEqual(yellow_successor_list, test_yellow_team_successors)

        test_purple_team_sucessors = [(1, [[0, 0, 0, 0, 0, 0], [0, -1, 1, 1, 1, 0], [0, 0, -1, -1, 0, 1], [1, -1, 0, 0, 0, 0], [-1, -1, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0]]),
                                      (1, [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, -1, -1, -1, 0, 1], [1, -1, 0, 0, 0, -1], [-1, -1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]]),
                                      (1, [[0, 0, 0, 0, 0, 0], [0, 0, -1, 1, 1, 0], [0, 0, -1, -1, 0, 1], [1, -1, 0, 0, 0, 0], [-1, -1, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0]]),
                                      (1, [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, -1, 0], [0, -1, -1, 0, 0, 1], [1, -1, 0, 0, 0, 0], [-1, -1, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0]]),
                                      (1, [[0, 0, 0, 0, 0, 0], [0, 0, -1, 1, 1, 0], [0, -1, -1, 0, 0, 1], [1, -1, 0, 0, 0, 0], [-1, -1, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0]]),
                                      (1, [[0, 0, 0, 0, 0, 0], [0, 0, 1, -1, 1, 0], [0, -1, 0, -1, 0, 1], [1, -1, 0, 0, 0, 0], [-1, -1, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0]]),
                                      (1, [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, -1, -1, -1, 0, 1], [-1, -1, 0, 0, 0, 0], [-1, 0, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0]])]

        compare_purple_team = (teams['Purple'], reference_board_state)
        test_board.board_position_assigner(compare_purple_team)
        purple_successor_list = test_board.successor_generator()
        self.assertEqual(purple_successor_list, test_purple_team_sucessors)
        print('succesful move test')

    def toggle(self, state):
        turn, board = state
        turn *=-1
        new_state = (turn,) + state[1:]
        return new_state

    def winning_positions(self):
        test_board = Board()
        teams = {'Purple': -1,
                 'Yellow': 1}


        reference_board_states0 = (1,[[0, 0, 0, 0, -1, 0],
                                       [0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0],
                                       [0, 1, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0]])

        reference_board_states1 = (1, [[0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, -1, 0],
                                      [0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0],
                                      [0, 1, 0, 0, 0, 0]])

        reference_board_states2 = (1, [[0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 1],
                                      [0, 0, 0, 1, 0, -1],
                                      [0, 1, 0, -1, 0, 0],
                                      [0, -1, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0]])

        reference_board_states3 = (-1,[[0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0],
                                      [0, 1, 0, 1, 0, 0],
                                      [0, 0, 0, 0, 1, 0],
                                      [0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0]])

        reference_board_states4 = (1, [[0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0],
                                       [0, -1, 0, -1, 0, 0],
                                       [0, 0, 0, 0, -1, 0],
                                       [0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0]])


        terminal_state_value = test_board.utility_statics(reference_board_states0)
        self.assertEqual(terminal_state_value, -100)

        terminal_state_value = test_board.utility_statics(reference_board_states1)
        self.assertEqual(terminal_state_value, 100)

        terminal_state_value = test_board.utility_statics(reference_board_states2)
        self.assertEqual(terminal_state_value, -100)

        terminal_state_value = test_board.utility_statics(reference_board_states4)
        self.assertEqual(terminal_state_value, -100)

        print('Test Yellow Team done')


        terminal_state_value = test_board.utility_statics(self.toggle(reference_board_states0))
        self.assertEqual(terminal_state_value, 100)

        terminal_state_value = test_board.utility_statics(self.toggle(reference_board_states1))
        self.assertEqual(terminal_state_value, -100)

        terminal_state_value = test_board.utility_statics(self.toggle(reference_board_states2))
        self.assertEqual(terminal_state_value, -100)

        terminal_state_value = test_board.utility_statics(reference_board_states3)
        self.assertEqual(terminal_state_value, -100)
        print('Test Purple Team done')

        print('unit test succesful')




