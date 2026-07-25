class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        if len(nums) == 0:
            return 0

        longest = 1

        for i in num_set:
            count = 0
            if i-1 not in num_set:
                count = 1
                while count + i in num_set:
                    count += 1
                    longest = max(longest, count)

        return longest