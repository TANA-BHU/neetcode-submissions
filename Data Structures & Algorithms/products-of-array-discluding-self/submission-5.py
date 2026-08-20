class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
          # Left to Right
        output = [1]*len(nums)
        pre = 1
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        return output
        
