from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        max_w = 0
        l, r = 0, 0
        while r < len(s):
            freq_map[s[r]] += 1
            maxf = max(freq_map.values())
            L = (r - l) + 1
            if (L - maxf) > k:
                freq_map[s[l]] -= 1
                l += 1
            max_w = max(max_w, r - l + 1)
            r += 1
        return max_w



        