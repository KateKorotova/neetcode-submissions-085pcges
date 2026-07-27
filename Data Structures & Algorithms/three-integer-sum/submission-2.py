class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numHash = {}
        res = set()
        for i in range(len(nums)):
            target = -nums[i]
            for j in range(i+1, len(nums)):
                complement = target - nums[j]
                if complement in numHash and numHash[complement] != i and numHash[complement] != j:
                    res.add(tuple(sorted([nums[i],nums[j], complement])))
                else:
                    numHash[nums[j]] = j
            numHash[nums[i]] = i
        return list(res)
