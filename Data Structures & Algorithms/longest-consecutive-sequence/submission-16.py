class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0
        for num in nums_set:
            if num-1 not in nums_set:
                start = num
                seq = 1
                while start+1 in nums_set:
                    seq += 1
                    start = start+1
                max_seq = max(max_seq, seq)
        return max_seq
