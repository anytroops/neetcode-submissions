class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        window = {}
        req = len(need)
        formed = 0
        bestLen = float('inf')
        bestL, bestR = 0, 0
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in need and need[s[r]] == window[s[r]]:
                formed += 1
            while formed == req:
                if r - l < bestLen:
                    bestLen = r - l + 1
                    bestL = l
                    bestR = r
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
        
        if bestLen != float('inf'):
            return s[bestL:bestR + 1]
        return ""




        