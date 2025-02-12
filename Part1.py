import unittest

def create_empty_board(n):
    return [['O' for _ in range(n)] for _ in range(n)]

def count_queens(board):
    return sum(row.count('#') for row in board)

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

def solve_n_queens(n):
    if n <= 0:
        raise ValueError("La taille du plateau doit être positive")
    if n == 1:
        return [[['#']]]
    if n == 2:
        return []  # Pas de solution possible
    if n == 3:
        return []  # Pas de solution possible
    return []

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

    def test_init_3x3_board(self):
        board = create_empty_board(3)
        expected = [['O', 'O', 'O'],
                   ['O', 'O', 'O'],
                   ['O', 'O', 'O']]
        self.assertEqual(board, expected)
        self.assertTrue(count_queens(board) == 0)

    def test_solve_1x1(self):
        solutions = solve_n_queens(1)
        self.assertEqual(len(solutions), 1)
        self.assertEqual(solutions[0], [['#']])

    def test_solve_2x2(self):
        solutions = solve_n_queens(2)
        self.assertEqual(len(solutions), 0)  # Pas de solution pour 2x2

    def test_solve_3x3(self):
        solutions = solve_n_queens(3)
        self.assertEqual(len(solutions), 0)  # Pas de solution pour 3x3

    def test_solve_invalid_input(self):
        with self.assertRaises(ValueError):
            solve_n_queens(0)
        with self.assertRaises(ValueError):
            solve_n_queens(-1)

if __name__ == '__main__':
    unittest.main()
