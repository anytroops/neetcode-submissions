class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        seen = {}
        def back(r, c):
            if (r,c) in seen:
                return seen[(r,c)]
            if r == m - 1 and c == n - 1:
                return 1
            if r == m or c == n:
                return 0
            seen[(r,c)] = (back(r, c + 1) + back(r + 1, c))
            return seen[(r,c)]
        return back(0,0)
        