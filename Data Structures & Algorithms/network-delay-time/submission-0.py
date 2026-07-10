class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        
        for source, destination, weight in times:
            graph[source].append((destination, weight))

        minHeap = [(0,k)]
        visited = set()
        maxTime = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            maxTime = max(time, maxTime)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (time + weight, neighbor))



        if len(visited) == n:
            return maxTime
        return -1
        