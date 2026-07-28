class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        curr_max = 0
        for price in prices:
            curr_max = max(curr_max, price - curr_min)
            curr_min = min(price, curr_min)
        return curr_max
                


        