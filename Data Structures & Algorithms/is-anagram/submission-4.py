class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        for element in s:
            if element in s_map:
                s_map[element] += 1
            else:
                s_map[element] = 1
        for element in t:
            if element in s_map:
                s_map[element] -= 1
            else:
                return False
        for element, count in s_map.items():
            if count != 0:
                return False
        return True