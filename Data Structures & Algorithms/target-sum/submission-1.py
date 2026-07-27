class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        seen = {}
        def back(i, curr):
            if (i, curr) in seen:
                return seen[(i, curr)]
            if i == len(nums):
                if curr == target:
                    return 1
                return 0
            seen[(i, curr)] = back(i + 1, curr + nums[i]) + back(i + 1, curr - nums[i])
            return seen[(i, curr)]
        return back(0, 0)
        