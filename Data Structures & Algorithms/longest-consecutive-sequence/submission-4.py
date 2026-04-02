class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if not nums:
            return 0
        max_len = 1
        curr_len = 1
        print(nums)
        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i-1]) == 1:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 1
        return max(max_len, curr_len)
