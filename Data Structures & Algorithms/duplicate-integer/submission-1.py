from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1
        # return any(x > 1 for x in count.values())
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False



        