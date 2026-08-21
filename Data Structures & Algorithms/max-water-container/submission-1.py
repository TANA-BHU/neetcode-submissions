class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        lp = 0 
        rp = len(heights) - 1
        while lp < rp :
            height = min(heights[lp], heights[rp])
            width = rp - lp
            area = height * width
            max_area = max(max_area, area)

            if (heights[lp] < heights[rp]):
                lp += 1
            else:
                rp -= 1
        return max_area
