class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        highest = 0
        for i in range(len(nums)-1):
            if nums[i] == (nums[i+1] - 1):
                count += 1
                if highest < count:
                    highest = count
            else:
                count =1

        return highest +1

        