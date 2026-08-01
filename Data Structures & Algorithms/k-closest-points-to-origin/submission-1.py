import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap, (dist, point))
        for i in range(k):
            closest = heapq.heappop(heap)
            ans.append(closest[1])
        return ans