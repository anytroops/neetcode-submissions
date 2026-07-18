class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = {}
        def back(i):
            if i == len(s):
                return True
            if i in seen:
                return seen[i]
            for word in wordDict:
                if word == s[i:i + len(word)]:
                    if back(i + len(word)):
                        return True
            seen[i] = False
            return False
        return back(0)
        