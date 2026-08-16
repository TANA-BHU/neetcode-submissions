class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for s in strs:
            counter = [0] * 26
            for ch in s:
                idx = ord(ch) - ord('a')
                counter[idx] += 1

            d_keys = tuple(counter)
            if d_keys not in output:
                output[d_keys] = [s]
            else:
                output[d_keys].append(s)
        return list(output.values())