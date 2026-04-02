from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if target - nums[i] == nums[j]:
        #             return [i, j]
        indexes = {}
        for i in range(len(nums)):
            if nums[i] not in indexes:
                indexes[nums[i]] = [i]
            else:
                indexes[nums[i]].append(i)
        print(indexes)
        for index, num in enumerate(nums):
            look = target - num
            if (look in indexes):
                if look != num:
                    return [index, min(indexes[look])]
                elif len(indexes[look]) > 1:
                    return [index, max(indexes[look])]
        return None
            