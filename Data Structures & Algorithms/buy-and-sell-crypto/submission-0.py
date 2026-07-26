class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0
        r = 0

        profit = 0

        while r < len(prices):
            while l < r:
                if prices[r] - prices[l] > 0:
                    profit = prices[r] - prices[l]
                    break
                l+=1
            r +=1
            maxProfit = max(maxProfit, profit)

        return maxProfit
        