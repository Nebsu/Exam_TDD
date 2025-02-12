import unittest

def create_empty_board(n):
    return [['O' for _ in range(n)] for _ in range(n)]
    
def is_attacking(pos1, pos2):
    row1, col1 = pos1
    row2, col2 = pos2

    if row1 == row2 or col1 == col2:
        return True

    if abs(row1 - row2) == abs(col1 - col2):
        return True
        
    return False

class TestSingleAttackQueens(unittest.TestCase):

    def test_init_board(self):
        expected = [['O', 'O', 'O', 'O'],
                   ['O', 'O', 'O', 'O'],
                   ['O', 'O', 'O', 'O'],
                   ['O', 'O', 'O', 'O']]
        self.assertEqual(create_empty_board(4), expected)

    def test_multiple_positions(self):
        # Test positions qui ne s'attaquent pas mutuellement
        positions = [
            ((0, 0), (1, 2)),
            ((0, 1), (2, 2)),
            ((1, 1), (3, 0))
        ]
        for pos1, pos2 in positions:
            self.assertFalse(is_attacking(pos1, pos2))

        attack_positions = [
            ((0, 0), (0, 3)),  # même ligne
            ((0, 0), (3, 0)),  # même colonne
            ((0, 0), (2, 2)),  # diagonale
            ((3, 0), (0, 3))   # diagonale inverse
        ]
        for pos1, pos2 in attack_positions:
            self.assertTrue(is_attacking(pos1, pos2))

if __name__ == '__main__':
    unittest.main()
