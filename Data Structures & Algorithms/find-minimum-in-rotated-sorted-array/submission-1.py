class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_ele = float('inf')

        lp, rp = 0, len(nums) - 1

        while lp<=rp:
            mid = (lp + rp) // 2
            if(nums[lp] <= nums[mid]):
                min_ele = min(min_ele, nums[lp])
                lp = mid + 1
            else:
                min_ele = min(min_ele, nums[mid])
                rp = mid - 1
        return min_ele