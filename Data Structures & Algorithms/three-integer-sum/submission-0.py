class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
        return list(result)