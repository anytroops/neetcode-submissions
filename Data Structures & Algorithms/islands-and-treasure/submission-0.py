from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1,0), (0,1), (-1, 0), (0, -1)]:
                row = dr + r
                col = dc + c
                if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == -1 or grid[row][col] != 2147483647:
                    continue
                grid[row][col] = grid[r][c] + 1
                queue.append((row, col))
        

        