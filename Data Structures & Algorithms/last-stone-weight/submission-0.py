class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-i for i in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            y = -heapq.heappop(neg_stones)
            x = -heapq.heappop(neg_stones)
            if x != y:
                heapq.heappush(neg_stones, -abs(x-y))
        return -neg_stones[0] if neg_stones else 0
