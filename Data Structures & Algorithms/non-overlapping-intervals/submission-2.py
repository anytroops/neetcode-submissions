class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        count = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prevEnd:
                count += 1
            else:
                prevEnd = end
        return count
        