class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        lp = 0
        ans = 0
        freq = {}
        max_freq = 0

        for rp in range(len(s)):

            if s[rp] not in freq:
                freq[s[rp]] = 0
            freq[s[rp]] += 1

            max_freq = max(freq.values())

            wind_size = rp - lp + 1
            rep = wind_size - max_freq

            while rep > k:
                freq[s[lp]] -= 1
                lp += 1

                wind_size = rp - lp + 1
                rep = wind_size - max_freq
            ans = max(ans, wind_size)

        return ans