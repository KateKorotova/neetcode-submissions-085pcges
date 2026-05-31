class Solution:
    def returnSquareSum(self, n):
        digits_array = [int(d) for d in str(n)]
        return sum([i*i for i in digits_array])

    def isHappy(self, n: int) -> bool:
        curr_num = self.returnSquareSum(n)
        print(curr_num)
        seen_num = set()
        while curr_num not in seen_num:
            if curr_num == 1:
                return True
            seen_num.add(curr_num)
            curr_num = self.returnSquareSum(curr_num)
        return False

        