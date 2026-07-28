class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_idx = {}
        max_len = 0
        start = 0

        for i in range(len(s)):
            if s[i] not in hash_idx or hash_idx[s[i]] < start:
                hash_idx[s[i]] = i 
            else:
                max_len = max(max_len, i-start)
                start = hash_idx[s[i]] + 1
                hash_idx[s[i]] = i
        return  max(max_len, len(s)-start)
