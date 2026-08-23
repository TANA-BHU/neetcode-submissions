class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_ele = float('inf')

        for num in nums:
            if min_ele > num:
                min_ele = num
        return min_ele