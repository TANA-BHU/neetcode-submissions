class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        for i in nums:
            if i in output:
                output[i] += 1
            else:
                output[i] = 1
        sorted_d = dict(sorted(output.items(), key=lambda x:x[1], reverse=True))
        top_k = list(sorted_d.keys())[:k]
        return top_k