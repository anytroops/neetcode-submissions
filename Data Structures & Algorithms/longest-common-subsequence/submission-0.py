class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        seen = {}
        def back(i, j):
            if (i, j) in seen:
                return seen[(i,j)]
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                seen[(i,j)] = 1 + back(i + 1, j + 1)
            else:
                seen[(i, j)] = max(back(i + 1, j), back(i, j + 1))
            return seen[(i,j)]
        return back(0,0)
        