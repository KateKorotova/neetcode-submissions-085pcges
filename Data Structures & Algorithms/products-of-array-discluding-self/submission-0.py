class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1]*(len(nums)+1)
        suffix_prod = [1]*len(nums)
        for i in range(1, len(nums)):
            prefix_prod[i] = nums[i-1]*prefix_prod[i-1]
            suffix_prod[-i-1] = nums[-i]*suffix_prod[-i]
        result = []
        print(prefix_prod)
        print(suffix_prod)
        for i in range(len(nums)):
            result.append(prefix_prod[i]*suffix_prod[i])
        return result
