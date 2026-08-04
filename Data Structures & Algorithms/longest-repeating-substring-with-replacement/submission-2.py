class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        freq = {}
        start = 0
        max_len = 0

        for i in range(len(s)):
            char = s[i]
            freq[char] = freq.get(char, 0) + 1

            max_freq = max(max_freq, freq[char])

            while (i - start + 1) - max_freq > k:
                freq[s[start]] -= 1
                start += 1

            max_len = max(max_len, i - start + 1)

        return max_len
