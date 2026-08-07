class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = [False] * 3
        for tri in triplets:
            if tri[0] > target[0] or tri[1] > target[1] or tri[2] > target[2]:
                continue
            for i in range(3):
                if tri[i] == target[i]:
                    good[i] = True
        return all(good)
        