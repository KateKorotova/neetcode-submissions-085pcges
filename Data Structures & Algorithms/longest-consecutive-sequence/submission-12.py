class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_seq = 0
        for num in nums:
            start = num
            curr_len = 0
            while start in set_nums:
                curr_len += 1
                start += 1
            max_seq = max(max_seq, curr_len)
        return max_seq
