class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        seen = {}
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        def back(i, currSum):
            key = (i, currSum)
            if key in seen:
                return seen[key]
            if currSum == target:
                return True
            if currSum > target or i == len(nums):
                return False
            seen[key] = (back(i + 1, currSum) or back(i + 1, currSum + nums[i]))
            return seen[key]
        return back(0, 0)
            
        