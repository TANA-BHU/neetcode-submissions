class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        #creat buckets
        n = len(nums)
        bucket = [[]for i in range(n+1)]

        for num,bucket_id in freq.items():
            bucket[bucket_id].append(num)
        
        #return top_k
        result = []
        for bucket_id in range(n,0,-1):
            for num in bucket[bucket_id]:
                result.append(num)
                if (len(result) == k):
                    return result
