"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import timeit

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer()
        self.player2 = game_agent.MinimaxPlayer()
        self.game = isolation.Board(self.player1, self.player2)
        self.time_millis = lambda: 1000 * timeit.default_timer()

    def test_minimax(self):
        move_start = self.time_millis()
        time_limit = 5000
        time_left = lambda : time_limit - (self.time_millis() - move_start)
        self.assertEqual(self.player1.get_move(self.game, time_left), (0, 0))



if __name__ == '__main__':
    unittest.main()
