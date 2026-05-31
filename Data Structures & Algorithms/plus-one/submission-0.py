class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ones = 1
        res = []
        for digit in digits[::-1]:
            new_n = digit
            if ones > 0:
                if digit == 9:
                    new_n = 0
                else:
                    new_n += 1
                    ones -= 1
            res.append(new_n)
        if ones > 0:
            res.append(1)
        return list(reversed(res))
            
            

