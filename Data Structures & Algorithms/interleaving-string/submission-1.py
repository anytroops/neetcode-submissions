class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        seen = {}
        def back(i, j):
            if (i,j) in seen:
                return seen[(i,j)]
            seen[(i,j)] = False
            if i == len(s1) and j == len(s2):
                return True
            if i < len(s1) and s1[i] == s3[i + j]:
                seen[(i,j)] = back(i + 1, j)
            if not seen[(i,j)] and j < len(s2) and s2[j] == s3[i +j]:
                seen[(i,j)] = back(i, j + 1)
            return seen[(i,j)]
        return back(0,0)

        