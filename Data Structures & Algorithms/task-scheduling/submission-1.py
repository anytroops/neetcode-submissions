import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-freq for freq in count.values()]
        heapq.heapify(maxHeap)
        cooldown = deque()
        time = 0
        while maxHeap or cooldown:
            time += 1
            if cooldown and cooldown[0][1] == time:
                count, _ = cooldown.popleft()
                heapq.heappush(maxHeap, count)
            if maxHeap:
                rem = heapq.heappop(maxHeap)
                rem += 1
                if rem < 0:
                    cooldown.append((rem, time + n + 1))
        return time