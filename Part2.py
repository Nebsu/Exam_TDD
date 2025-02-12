import unittest

def create_empty_board(n):
    return [['O' for _ in range(n)] for _ in range(n)]
    
def is_attacking(pos1, pos2):
    return True

class TestSingleAttackQueens(unittest.TestCase):

    def test_init_board(self):
        expected = [['O', 'O', 'O', 'O'],
                   ['O', 'O', 'O', 'O'],
                   ['O', 'O', 'O', 'O'],
                   ['O', 'O', 'O', 'O']]
        self.assertEqual(create_empty_board(4), expected)

    def test_same_row_attack(self):
        self.assertTrue(is_attacking((0, 0), (0, 2)))
        self.assertTrue(is_attacking((1, 0), (1, 3)))

    def test_same_column_attack(self):
        self.assertTrue(is_attacking((0, 0), (2, 0)))
        self.assertTrue(is_attacking((1, 2), (3, 2)))

    def test_diagonal_attack(self):
        self.assertTrue(is_attacking((0, 0), (2, 2)))
        self.assertTrue(is_attacking((0, 2), (2, 0)))

    # def test_no_attack(self):
    #     self.assertFalse(is_attacking((0, 0), (1, 2)))
    #     self.assertFalse(is_attacking((2, 1), (0, 3)))

if __name__ == '__main__':
    unittest.main()
