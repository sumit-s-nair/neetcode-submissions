class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_vol = 0
        n = len(heights)
        left = 0
        right = n - 1

        while left < right:
            base = right - left
            max_vol = max(min(heights[left], heights[right]) * base, max_vol)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_vol            
        