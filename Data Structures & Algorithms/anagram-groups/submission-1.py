class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for s in strs:
            temp = "".join(sorted(s))
            if temp not in output:
                output[temp] = [s]
            else:
                output[temp].append(s)
        return list(output.values())