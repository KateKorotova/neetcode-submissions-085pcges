class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_w = 0
        left, right = 0, len(heights) - 1
        while left < right:
            min_h = min(heights[left], heights[right])
            max_w = max(max_w, (right - left)*min_h)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_w