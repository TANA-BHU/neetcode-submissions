class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        n = len(s)
        i = 0
        while i<n:
            j = i
            while s[j] != "#":
                j += 1
            exact_len = int(s[i:j])
            i = j + 1
            strs = s[i:i + exact_len]
            decoded_strs.append(strs)
            i += exact_len
        return decoded_strs