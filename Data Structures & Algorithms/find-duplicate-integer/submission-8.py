class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set_num = set()
        for num in nums:
            if num in set_num:
                return num 
            set_num.add(num)