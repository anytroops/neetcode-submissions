class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            one = nums[0]
            two = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                curr = max(two, one + nums[i])
                one= two
                two = curr
            return two
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))