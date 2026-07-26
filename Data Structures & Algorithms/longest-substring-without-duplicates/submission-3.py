class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_s = 0

        for i in range(len(s)):
            char = s[i]
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            
            seen[char] = i
            max_s = max(max_s, i - left + 1)

            
        return max_s