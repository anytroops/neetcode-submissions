import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [(0,0)]
        visited = set()
        total = 0
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            total += cost
            for nextNode in range(len(points)):
                x1, y1 = points[node]
                if nextNode not in visited:
                    x2, y2 = points[nextNode]
                    distance = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(minHeap, (distance, nextNode))
            if len(visited) == len(points):
                return total

        