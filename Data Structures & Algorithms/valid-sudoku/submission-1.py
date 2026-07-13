class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        squares = set()
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                val = board[r][c]
                if (val, r) in rows or (val, c) in cols or (val, r//3, c// 3) in squares:
                    return False
                rows.add((val, r))
                cols.add((val, c))
                squares.add((val, r//3, c//3))
        return True
        