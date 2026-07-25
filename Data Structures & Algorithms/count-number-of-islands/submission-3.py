class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        islands= 0
        def back(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0" or (r,c) in seen:
                return
            seen.add((r,c))
            back(r + 1, c)
            back(r - 1, c)
            back(r, c + 1)
            back(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in seen and grid[r][c] == "1":
                    back(r, c)
                    islands += 1
        return islands

