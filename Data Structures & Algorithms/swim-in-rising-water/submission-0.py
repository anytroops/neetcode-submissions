import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(grid[0][0], 0, 0)]
        visited = set()
        
        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            visited.add((r,c))
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return time
            for dr, dc in [(1 ,0), (0, 1), (-1, 0), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue
                if (nr, nc) not in visited:
                    heapq.heappush(minHeap, (max(time, grid[nr][nc]), nr, nc))
        