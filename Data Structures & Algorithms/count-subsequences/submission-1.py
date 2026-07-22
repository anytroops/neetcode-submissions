class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        seen = {}
        def back(i,j):
            if (i,j) in seen:
                return seen[(i,j)]
            if j == len(t):
                return 1
            if i == len(s) and j != len(t):
                return 0
            if s[i] == t[j]:
                seen[(i,j)] = back(i + 1, j + 1) + back(i + 1, j)
            else:
                seen[(i,j)] = back(i + 1, j)
            return seen[(i,j)]
        return back(0,0)