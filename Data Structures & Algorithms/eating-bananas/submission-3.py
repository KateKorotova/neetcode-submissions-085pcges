import math 

class Solution:
    def getRate(self, piles, k):
        return sum(math.ceil(x/k) for x in piles)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = float('inf')
        while l <= r:
            mid = l + ((r-l)//2)
            k = self.getRate(piles, mid)
            if k <= h:
                r = mid - 1
                res = min(res, mid) 
            elif k > h:
                l = mid + 1
        return res


