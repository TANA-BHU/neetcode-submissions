class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        lp = 0 
        rp = len(heights) - 1
        while lp < rp :

            max_area = max(min(heights[lp], heights[rp]) * (rp - lp) , max_area)

            if (heights[lp] < heights[rp]):
                lp += 1
            else:
                rp -= 1
        return max_area
