import unittest

class TestNQueens(unittest.TestCase):
    def test_same_row(self):
        board = [['#', '#', 'O'],
                ['O', 'O', 'O'],
                ['O', 'O', 'O']]
        self.assertTrue(self.has_conflict(board))

    def test_same_column(self):
        board = [['#', 'O', 'O'],
                ['#', 'O', 'O'],
                ['O', 'O', 'O']]
        self.assertTrue(self.has_conflict(board))

    def test_same_diagonal(self):
        board1 = [['#', 'O', 'O'],
                 ['O', '#', 'O'],
                 ['O', 'O', 'O']]
        self.assertTrue(self.has_conflict(board1))

        board2 = [['O', 'O', '#'],
                 ['O', '#', 'O'],
                 ['O', 'O', 'O']]
        self.assertTrue(self.has_conflict(board2))

    def test_valid_placement(self):
        board = [['#', 'O', 'O'],
                ['O', 'O', '#'],
                ['O', 'O', 'O']]
        self.assertFalse(self.has_conflict(board))

if __name__ == '__main__':
    unittest.main()
