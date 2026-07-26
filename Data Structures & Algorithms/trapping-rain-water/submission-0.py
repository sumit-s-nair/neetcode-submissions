class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = []
        blue = 0

        for i in range(len(height)):
            left = 0
            right = n-1
            max_left = 0
            max_right = 0
            while left < i or right > i:
                max_left = max(height[left], max_left)
                max_right = max(height[right], max_right)
                if left < i:
                    left += 1
                if right > i:
                    right -= 1
            if max_right and max_left and max_left > height[i] and max_right > height[i]:
                water.append([height[i], max_left, max_right])

        print(water)

        for i in water:
            blue = blue + min(i[1], i[2]) - i[0]

        return blue
        
                