class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ret = []
        atlantic = set()
        pacific = set()
        rows = len(heights)
        cols = len(heights[0])
        def dfs(r, c, visited, prevHeight):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or heights[r][c] < prevHeight:
                return
            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    dfs(r, c, pacific, 0)
                if r == rows - 1 or c == cols - 1:
                    dfs(r, c, atlantic, 0)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    ret.append((r,c))
        return ret
        