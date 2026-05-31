class Solution:
    def returnSquareSum(self, n):
        digits_array = [int(d) for d in str(n)]
        return sum([i*i for i in digits_array])
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.returnSquareSum(n)
        while fast != 1 and fast != slow: 
            slow =  self.returnSquareSum(slow)
            fast =  self.returnSquareSum(self.returnSquareSum(fast))
        return fast == 1