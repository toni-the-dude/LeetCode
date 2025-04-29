class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        global_min = prices[0]
        profit = 0

        for price in prices[1:]:
            if price < global_min:
                global_min = price
            elif price - global_min > profit:
                profit = price - global_min
            
        return profit