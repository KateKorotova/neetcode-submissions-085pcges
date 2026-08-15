from collections import defaultdict 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        freq_s1 = defaultdict(int)
        check_freq = defaultdict(int)
        w_s = len(s1)
        for i in range(w_s):
            freq_s1[s1[i]] += 1 
            check_freq[s2[i]] += 1 

        for i in range(len(s2) - w_s):
            if freq_s1 == check_freq:
                return True
            if check_freq[s2[i]] > 1:
                check_freq[s2[i]] -= 1
            else:
                del check_freq[s2[i]]
            check_freq[s2[i + w_s]] += 1
        
        return freq_s1 == check_freq
            
