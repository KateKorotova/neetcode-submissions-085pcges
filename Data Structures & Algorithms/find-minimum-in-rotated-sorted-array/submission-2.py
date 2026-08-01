class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return nums[0]
        while left < right:
            mid = (left+right)//2
            # print(nums[mid])
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid 
            # print(nums[left], nums[right])
        return nums[left]

