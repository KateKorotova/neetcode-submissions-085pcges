from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        countMap = defaultdict(int)
        res = set()
        for num in nums:
            countMap[num] += 1
        for i in range(len(nums)):
            countMap[nums[i]] -= 1
            for j in range(i + 1, len(nums)):
                countMap[nums[j]] -= 1
                target = -(nums[i] + nums[j])
                if target in countMap and countMap[target] > 0:
                    res.add(tuple(sorted([nums[i], nums[j], target])))
                countMap[nums[j]] += 1
            countMap[nums[i]] += 1
        return list(res)