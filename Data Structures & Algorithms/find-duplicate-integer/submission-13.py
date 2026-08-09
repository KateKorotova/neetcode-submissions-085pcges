# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         for num in nums:
#             num_abs = abs(num)
#             if nums[num_abs - 1] < 0:
#                 returnnum_abs
#             nums[num_abs- 1] =  nums[num_abs - 1]*(-1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow] 
            fast = nums[nums[fast]]

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow
