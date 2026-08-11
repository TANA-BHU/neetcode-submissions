class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map ={}
        for ele in s:
            if ele in s_map:
                s_map[ele] += 1
            else:
                s_map[ele] = 1
        for ele in t:
            if ele in t_map:
                t_map[ele] += 1
            else:
                t_map[ele] = 1
        return s_map == t_map