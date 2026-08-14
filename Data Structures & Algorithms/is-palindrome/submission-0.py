class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        
        for ch in s:
            if ch.isalnum():
                new_s += ch.lower()
        lp, rp = 0, len(new_s)-1
        while lp<rp:
            if new_s[lp] != new_s[rp]:
                return False
            lp += 1
            rp -= 1
        return True