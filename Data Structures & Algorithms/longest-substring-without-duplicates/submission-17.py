class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx_map = {}
        max_subs = 0
        start_seq = 0
        for i in range(len(s)):
            if s[i] in idx_map and idx_map[s[i]] >= start_seq:
                max_subs = max(max_subs, i - start_seq)
                start_seq = idx_map[s[i]] + 1
            idx_map[s[i]] = i
        return max(max_subs, len(s) - start_seq)
            
