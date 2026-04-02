class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_w = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         water = (j-i)*min(heights[i], heights[j])
        #         if water > max_w:
        #             max_w = water
        # return max_w
        max_w = 0
        i, j = 0,len(heights) - 1
        while i < j:
            water = (j-i)*min(heights[i], heights[j])
            if water > max_w:
                max_w = water
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max_w

            
