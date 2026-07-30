class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        window = {}
        bestL, bestR = 0, 0
        bestLen = float('inf')
        l = 0
        req = len(need)
        have = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in need and window[s[r]] == need[s[r]]:
                have += 1
            while req == have:
                if r - l < bestLen:
                    bestLen = r - l + 1
                    bestR = r
                    bestL = l
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        if bestLen != float('inf'):
            return s[bestL:bestR + 1]  
        return ""




        