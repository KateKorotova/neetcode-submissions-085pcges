class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_sum = 0
        # last_neg_index = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            curr_max = max(curr_max, curr_sum)
            if curr_sum < 0:
                curr_sum = 0

        return curr_max
