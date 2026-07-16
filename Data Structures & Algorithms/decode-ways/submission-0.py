class Solution:
    def numDecodings(self, s: str) -> int:
        seen = {}
        def ways(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in seen:
                return seen[i]

            out = ways(i + 1)

            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6")):
                out += ways(i + 2)
            
            seen[i] = out
            return out
        
        return ways(0)