class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right, left = 0, len(numbers) - 1 
        while right < left:
            curr_sum = numbers[right]+numbers[left]
            if curr_sum == target:
                return [right + 1, left + 1]
            elif curr_sum > target:
                left -= 1
            else:
                right += 1
        return []
        