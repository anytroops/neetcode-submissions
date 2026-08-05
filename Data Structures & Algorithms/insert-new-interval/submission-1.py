class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        for i, curr in enumerate(intervals):
            if curr[1] < newInterval[0]:
                merged.append(curr)
            elif curr[0] > newInterval[1]:
                merged.append(newInterval)
                return merged + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], curr[0])
                newInterval[1] = max(newInterval[1], curr[1])
        
        merged.append(newInterval)
        return merged

        