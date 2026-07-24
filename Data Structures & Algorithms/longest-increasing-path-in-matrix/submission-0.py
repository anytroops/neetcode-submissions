class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        seen = {}
        def back(r, c):
            if (r,c) in seen:
                return seen[(r,c)]
            longestPath = 1
            for dr, dc in [(1,0), (0,1), (-1,0), (0, -1)]:
                nr, nc = dr + r, dc + c
                if (0 <= nr < rows) and (0 <= nc < cols) and matrix[nr][nc] > matrix[r][c]:
                    longestPath = max(longestPath, 1 + back(nr, nc))
            seen[(r,c)] = longestPath
            return seen[(r,c)]
        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, back(r, c))
        return ans

        