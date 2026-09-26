import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            res = heapq.heappop_max(stones) - heapq.heappop_max(stones)

            if res > 0:
                heapq.heappush_max(stones, res)

        return stones[0] if stones else 0