class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sell = 0
        min_buy = float('inf')
        
        for i in prices:
            min_buy = min(min_buy, i)
            max_sell = max(max_sell, i - min_buy)

        return max_sell