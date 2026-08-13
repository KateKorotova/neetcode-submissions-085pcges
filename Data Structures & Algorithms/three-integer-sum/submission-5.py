class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i and nums[i-1] == nums[i]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1
                elif  nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j+= 1

        return res
                    



