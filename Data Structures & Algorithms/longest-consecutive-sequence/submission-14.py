class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort_nums = sorted(set(nums))
        print(sort_nums)
        if not nums:
            return 0
        max_len = 0
        curr_len = 1
        for i in range(1, len(sort_nums)):
            if (sort_nums[i-1] + 1) == sort_nums[i]:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 1
        return max(max_len, curr_len)


