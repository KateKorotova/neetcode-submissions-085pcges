class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_w = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                water = (j-i)*min(heights[i], heights[j])
                if water > max_w:
                    max_w = water
        return max_w