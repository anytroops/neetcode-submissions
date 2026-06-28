class Solution:
    def isPalindrome(self, s: str) -> bool:
        sList = [c.lower() for c in s if c.isalnum()]
        sList2 = sList[::-1]
        return sList == sList2
        