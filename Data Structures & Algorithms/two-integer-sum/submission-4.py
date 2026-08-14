class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_ele = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen_ele:
                return [seen_ele[complement], i]
            seen_ele[num] = i