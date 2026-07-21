class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        seen = {}
        def back(i, rem):
            if (i, rem) in seen:
                return seen[(i, rem)]
            if rem == 0:
                return 1
            if rem < 0 or i == len(coins):
                return 0
            seen[(i, rem)] = back(i, rem - coins[i]) + back(i + 1, rem)
            return seen[(i, rem)]
        return back(0, amount)
        