class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = nums[0]
        currMax = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            oldMin, oldMax = currMin, currMax
            currMax = max(nums[i], nums[i] * oldMin, nums[i] * oldMax)
            currMin = min(nums[i], nums[i] * oldMin, nums[i] * oldMax)
            res = max(res, currMax)
        return res
        