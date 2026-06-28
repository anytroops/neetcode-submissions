class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for j in range(len(nums)):
            if j > 0 and nums[j] == nums[j-1]:
                continue
            left, right = j + 1, len(nums) - 1
            while left < right:
                s = nums[j] + nums[left] + nums[right]
                if s == 0:
                    ret.append([nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return ret
            

        
        
        