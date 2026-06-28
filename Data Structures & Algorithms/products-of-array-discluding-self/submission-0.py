class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [1] * n
        leftStart = 1
        for i in range(n):
            ret[i] = leftStart
            leftStart *= nums[i]

        rightStart = 1
        for i in range(n-1, -1, -1):
            ret[i] *= rightStart
            rightStart *= nums[i]
        
        return ret



        