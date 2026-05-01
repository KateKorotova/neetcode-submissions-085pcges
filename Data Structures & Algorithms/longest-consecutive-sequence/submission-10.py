
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
        # nums_set = set(nums)
        # nums_list = list(set(nums))
        # max_len = 0
        # for num in nums_list:
        #     curr_len = 0
        #     curr = num
        #     while curr in nums_set:
        #         curr += 1
        #         curr_len +=1
        #     max_len = max(max_len, curr_len)
        # return max_len
        num_set = set(nums) #remove duplicate 2,20,4,10,3,5
        result = 0

        for n in nums:
            length = 0 
            while (n+length)  in num_set:
                length +=1
            result = max(result, length)
        return result

                