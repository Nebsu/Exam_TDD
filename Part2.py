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

def count_attacks(queens):
    attacks = {i: 0 for i in range(len(queens))}
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                attacks[i] += 1
                attacks[j] += 1
    return attacks

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

    def test_count_attacks_single(self):
        # Test avec deux reines qui s'attaquent
        queens = [(0, 0), (0, 2)]
        attacks = count_attacks(queens)
        self.assertEqual(attacks[0], 1)
        self.assertEqual(attacks[1], 1)

    def test_count_attacks_multiple(self):
        # Test avec quatre reines
        queens = [(0, 0), (1, 1), (2, 2), (3, 3)]
        attacks = count_attacks(queens)
        # Chaque reine attaque toutes les autres (diagonale)
        for i in range(4):
            self.assertEqual(attacks[i], 3)

    def test_count_attacks_no_attacks(self):
        # Test avec des reines qui ne s'attaquent pas
        queens = [(0, 0), (1, 2), (2, 4), (4, 1)]
        attacks = count_attacks(queens)
        for count in attacks.values():
            self.assertEqual(count, 0)

if __name__ == '__main__':
    unittest.main()
