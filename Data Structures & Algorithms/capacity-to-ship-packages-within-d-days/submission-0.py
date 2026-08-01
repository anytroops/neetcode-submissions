import math

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l < r:
            mid = (l + r) // 2
            currWeight = 0
            daysUsed = 1
            for weight in weights:
                if weight + currWeight <= mid:
                    currWeight += weight
                else:
                    daysUsed += 1
                    currWeight = weight
            if daysUsed <= days:
                r = mid
            else:
                l = mid + 1
        return l
        