class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []
        sort_list = sorted(nums)


        for i in range(len(sort_list)):

            if(i>0  and sort_list[i] == sort_list[i-1]): 
                continue
            left = i+1
            right = len(sort_list) - 1
            while(left < right):
                sum_three = sort_list[i] + sort_list[left] + sort_list[right]

                if(sum_three < 0):
                    left += 1

                elif(sum_three >0):
                    right -= 1

                else:
                    output.append([sort_list[i], sort_list[left], sort_list[right]])
                    left +=1 
                    right -= 1

                    while(left < right and sort_list[left] == sort_list[left-1]):
                        left += 1
                    while(left < right and sort_list[right] == sort_list[right+1]):
                        right -= 1
        return output

