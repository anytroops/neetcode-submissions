class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 1
        highest = 1
        for i in range(len(nums)-1):
            if nums[i] == (nums[i+1] - 1):
                count += 1
                highest = max(count, highest)
            elif nums[i] == nums[i+1]:  
                continue        
            else:
                count =1

        return highest 

        