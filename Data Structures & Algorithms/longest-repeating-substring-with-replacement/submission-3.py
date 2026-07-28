class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l = 0
        res = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            while (r - l + 1) - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
