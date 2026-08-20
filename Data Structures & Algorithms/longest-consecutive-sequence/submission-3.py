class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        s_len = 0
        max_len = 0

        for i in numSet:
            if (i-1) not in numSet:
                #start the sequence 
                s_len = 0
                while (i+s_len) in numSet:
                    s_len += 1
                max_len = max(s_len, max_len)
        return max_len
                
