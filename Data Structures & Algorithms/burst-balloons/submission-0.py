class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        seen = {}
        def back(l,r):
            if (l,r) in seen:
                return seen[(l,r)]
            if l > r:
                return 0
            maxCoins = 0
            for i in range(l, r + 1):
                coins = back(l, i -1) + back(i + 1, r) + nums[l - 1] * nums[i] * nums[r + 1]
                maxCoins = max(maxCoins, coins)
            seen[(l,r)] = maxCoins
            return seen[(l,r)]
        return back(1, len(nums) -2)
            

        