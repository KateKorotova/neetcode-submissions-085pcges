class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_s = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > curr_s:
                profit = max(profit, prices[i] - curr_s)
            else:
                curr_s = prices[i]
        return profit