class Solution:
    def checkValidString(self, s: str) -> bool:
        low, high = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                low += 1
                high += 1
            elif s[i] == ')':
                low -= 1
                high -= 1
            elif s[i] == '*':
                low -= 1
                high += 1
            low = max(low, 0)
            if high < 0:
                return False
        return low == 0