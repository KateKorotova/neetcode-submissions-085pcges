class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distances = []
        # for x, y in points:
        #     dist = math.sqrt((x**2) + (y**2))
        #     print(x, y, dist)
        #     distances.append((dist, [x, y]))
        distances = [(math.sqrt((x**2) + (y**2)), [x, y]) for x, y in points]
        heapq.heapify(distances)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(distances)[1])
        return res