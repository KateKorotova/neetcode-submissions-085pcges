class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        curr_max = 0
        for i in range(len(prices)):
            curr_max = max(curr_max, prices[i] - curr_min)
            curr_min = min(prices[i], curr_min)
        return curr_max
                


        