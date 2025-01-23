class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            diff = prices[r] - prices[l]
            
            print(l, r)

            if diff < 0:
                l = r
                r += 1
            else:
                r += 1
                max_profit = max(max_profit, diff)
        
        return max_profit
