class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        curr_set = dict()
        curr_start = 0
        max_len = 1
        for i in range(len(s)):
            if s[i] in curr_set:
                max_len = max(i - curr_start, max_len)
                curr_start = max(curr_set[s[i]] + 1, curr_start)
            curr_set[s[i]] = i
        return max(max_len, len(s) - curr_start)