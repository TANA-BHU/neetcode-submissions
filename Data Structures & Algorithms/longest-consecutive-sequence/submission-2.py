class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        sorted_arr = sorted(nums)

        current_count = 1
        max_count = 1

        for i in range(len(nums) - 1):

            if sorted_arr[i + 1] - sorted_arr[i] == 1:
                current_count += 1

            elif sorted_arr[i + 1] == sorted_arr[i]:
                continue

            else:
                current_count = 1

            max_count = max(max_count, current_count)

        return max_count