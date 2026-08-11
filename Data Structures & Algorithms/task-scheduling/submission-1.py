from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxf = max(count.values())
        maxCount = 0 
        for i in count.values():
            if i == maxf:
                maxCount += 1
        time = (maxf - 1)*(n+1) + maxCount
        return max(len(tasks), time)
