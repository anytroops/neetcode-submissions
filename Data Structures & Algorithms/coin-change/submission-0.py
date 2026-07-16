class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        seen = {}
        def back(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            if remaining in seen:
                return seen[remaining]
            best = float('inf')
            for coin in coins:
                best = min(best, 1 + back(remaining - coin))
            seen[remaining] = best
            return best

        ans = back(amount)
        if ans == float('inf'):
            return -1
        return ans
        