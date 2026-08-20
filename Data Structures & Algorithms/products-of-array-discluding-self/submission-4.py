class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
        if zero_count > 1:
            return [0]*len(nums)

        if zero_count == 1:
            prod = 1
            for num in nums:
                if num != 0:
                    prod *= num
            output = []
            for num in nums:
                if num == 0:
                    output.append(prod)
                else:
                    output.append(0)
            return output
            
        prod = 1
        for num in nums:
            prod *= num
        output = [prod // num for num in nums]
        return output

