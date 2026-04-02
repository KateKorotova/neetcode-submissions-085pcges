
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = sorted(set(nums))
        # if not nums:
        #     return 0
        # max_len = 1
        # curr_len = 1
        # print(nums)
        # for i in range(1, len(nums)):
        #     if abs(nums[i] - nums[i-1]) == 1:
        #         curr_len += 1
        #     else:
        #         max_len = max(max_len, curr_len)
        #         curr_len = 1
        # return max(max_len, curr_len)
        if not nums:
            return 0
        nums_set = set(nums)
        nums = list(set(nums))
        max_len = 1
        for num in nums:
            if (num - 1) not in nums_set:
                curr_len = 1
                check = True
                start = num 
                while check:
                    if start + 1 in nums_set:
                        start += 1
                        curr_len += 1
                    else:
                        check = False 
                        max_len = max(curr_len, max_len)
        return max_len

                