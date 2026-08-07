import heapq
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cards = Counter(hand)
        heap = list(cards.keys())
        heapq.heapify(heap)
        while heap:
            start = heap[0]
            for num in range(start, start + groupSize):
                if num not in cards or cards[num] ==0:
                    return False
                cards[num] -= 1
                if cards[num] == 0:
                    if num != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True