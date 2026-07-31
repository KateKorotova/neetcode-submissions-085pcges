import math 

class Solution:
    def get_h(self, piles, k):
        return sum(math.ceil(pile/k) for pile in piles)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right)//2
            curr_h = self.get_h(piles, mid)
            if curr_h <= h:
                right = mid
            elif curr_h > h:
                left = mid + 1
        return right
        

