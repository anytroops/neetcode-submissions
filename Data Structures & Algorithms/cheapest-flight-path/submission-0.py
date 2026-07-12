import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for source, destination, cost in flights:
            graph[source].append((destination, cost))
        minHeap = [(0, src, 0)]
        bestFlights = [float("inf")] * n
        while minHeap:
            cost, node, flightsUsed = heapq.heappop(minHeap)
            if flightsUsed > k + 1 or flightsUsed >= bestFlights[node]:
                continue
            if node == dst:
                return cost
            for neighbor, price in graph[node]:
                heapq.heappush(minHeap, (cost + price, neighbor, flightsUsed + 1))
        return -1




        