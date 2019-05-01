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
        yellow_successor_list = test_board.create_legal_moves()

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
        purple_successor_list = test_board.create_legal_moves()
        self.assertEqual(purple_successor_list, test_purple_team_sucessors)
        print('succesful move test')

    def winning_positions(self):
        test_board = Board()
        teams = {'Purple': -1,
                 'Yellow': 1}


        reference_board_states0 = [[0, 0, 0, 0, -1, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 1, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0]]

        reference_board_states1 = [[0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, -1, 0],
                                  [0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0]]

        reference_board_states2 = [[0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 1],
                                  [0, 0, 0, 1, 0, -1],
                                  [0, 1, 0, -1, 0, 0],
                                  [0, -1, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0]]

        reference_board_states3 = [[0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 1, 0, 0],
                                  [0, 0, 0, 0, 1, 0],
                                  [0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0]]

        reference_board_states4 = [[0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, -1, 0, -1, 0, 0],
                                   [0, 0, 0, 0, -1, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0]]

        test_board.default_team = teams['Yellow']
        compare_yellow_team = (teams['Yellow'], reference_board_states0)
        terminal_state_value = test_board.check_terminal_state(compare_yellow_team)
        self.assertEqual(terminal_state_value, -1)
        print('done')

        compare_yellow_team = (teams['Yellow'], reference_board_states1)
        terminal_state_value = test_board.check_terminal_state(compare_yellow_team)
        self.assertEqual(terminal_state_value, 1)
        print('done')

        compare_yellow_team = (teams['Yellow'], reference_board_states2)
        terminal_state_value = test_board.check_terminal_state(compare_yellow_team)
        self.assertEqual(terminal_state_value, -1)
        print('done')

        compare_yellow_team = (teams['Yellow'], reference_board_states4)
        terminal_state_value = test_board.check_terminal_state(compare_yellow_team)
        self.assertEqual(terminal_state_value, -1)

        print('yellow done')

        test_board.default_team = teams['Purple']
        compare_yellow_team = (teams['Purple'], reference_board_states0)
        terminal_state_value = test_board.check_terminal_state(compare_yellow_team)
        self.assertEqual(terminal_state_value, 1)
        print('done')

        compare_yellow_team = (teams['Purple'], reference_board_states1)
        terminal_state_value = test_board.check_terminal_state(compare_yellow_team)
        self.assertEqual(terminal_state_value, -1)
        print('done')

        compare_yellow_team = (teams['Purple'], reference_board_states2)
        terminal_state_value = test_board.check_terminal_state(compare_yellow_team)
        self.assertEqual(terminal_state_value, -1)
        print('done')

        compare_yellow_team = (teams['Purple'], reference_board_states3)
        terminal_state_value = test_board.check_terminal_state(compare_yellow_team)
        self.assertEqual(terminal_state_value, -1)
        print('done')

        print('winning position succesful')




