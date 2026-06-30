class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        seen = set()
        def dfs(row, col, i):
            if i == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in seen or board[row][col] != word[i]:
                return False
            seen.add((row, col))
            if dfs(row + 1, col, i +1) or dfs(row - 1, col, i + 1) or dfs(row, col + 1, i + 1) or dfs(row, col - 1, i + 1):
                return True
            seen.remove((row, col))
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
        