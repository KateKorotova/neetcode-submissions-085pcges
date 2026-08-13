class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashMap = {}
        res = set()
        for i in range(len(nums)):
            target = -nums[i]
            for j in range(i+1, len(nums)):
                complement = target - nums[j]
                if complement in hashMap and hashMap[complement] != i and hashMap[complement] != j:
                    res.add(tuple(sorted([nums[i], nums[j], complement])))
                hashMap[nums[j]] = j
            hashMap[nums[i]] = i
        return [triple for triple in res]