import unittest

def has_conflict(board):
    # Vérification des lignes
    for row in board:
        if row.count('#') > 1:
            return True
    
    # Vérification des colonnes
    n = len(board)
    for col in range(n):
        column_count = sum(1 for row in board if row[col] == '#')
        if column_count > 1:
            return True
    
    # Vérification des diagonales
    for i in range(n):
        for j in range(n):
            if board[i][j] == '#':
                # Vérifier toutes les autres positions
                for k in range(n):
                    for l in range(n):
                        # Ne pas comparer une position avec elle-même
                        if (k != i or l != j) and board[k][l] == '#':
                            # Vérifier si les positions sont sur la même diagonale
                            if abs(k - i) == abs(l - j):
                                return True
    return False

class TestNQueens(unittest.TestCase):
    def test_same_row(self):
        board = [['#', '#', 'O'],
                ['O', 'O', 'O'],
                ['O', 'O', 'O']]
        self.assertTrue(has_conflict(board))

    def test_same_column(self):
        board = [['#', 'O', 'O'],
                ['#', 'O', 'O'],
                ['O', 'O', 'O']]
        self.assertTrue(has_conflict(board))

    def test_same_diagonal(self):
        board1 = [['#', 'O', 'O'],
                 ['O', '#', 'O'],
                 ['O', 'O', 'O']]
        self.assertTrue(has_conflict(board1))

        board2 = [['O', 'O', '#'],
                 ['O', '#', 'O'],
                 ['O', 'O', 'O']]
        self.assertTrue(has_conflict(board2))

    def test_valid_placement(self):
        board = [['#', 'O', 'O'],
                ['O', 'O', '#'],
                ['O', 'O', 'O']]
        self.assertFalse(has_conflict(board))



if __name__ == '__main__':
    unittest.main()
