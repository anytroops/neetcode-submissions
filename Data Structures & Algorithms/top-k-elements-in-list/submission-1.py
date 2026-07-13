class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            buckets[count].append(num)
        
        ret = []
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                ret.append(num)
            if len(ret) == k:
                return ret
        