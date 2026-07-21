class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        seen = {}
        def back(i, canBuy):
            if (i, canBuy) in seen:
                return seen[(i, canBuy)]
            if i >= len(prices):
                return 0
            if canBuy == True:
                seen[(i, canBuy)] = max(-prices[i] + back(i + 1, False), back(i + 1, True))
            else:
                seen[(i, canBuy)] = max(prices[i] + back(i + 2, True), back(i + 1, False))
            return seen[(i, canBuy)]
        return back(0, True)
        