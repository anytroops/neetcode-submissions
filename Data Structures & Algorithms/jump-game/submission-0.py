class Solution:
    def canJump(self, nums: List[int]) -> bool:
        high = 0
        for i in range(len(nums)):
            if i > high:
                return False
            high = max(high, i + nums[i])
        return True
            
        