class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = [[-num, idx] for idx, num in enumerate(nums[:k])]
        heapq.heapify(heap)

        res.append(-heap[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(heap, [-nums[i], i])
            while heap[0][1] not in range(i-k+1, i+1):
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res