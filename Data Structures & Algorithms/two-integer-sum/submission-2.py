class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in seen:
                return [seen[compliment], i]
            seen[n] = i
        