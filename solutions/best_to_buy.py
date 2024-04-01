# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1220170661/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cheapest   = 10001
        max_profit = 0

        for i in range(0, len(prices)): 
            if cheapest > prices[i]:
                cheapest = prices[i]
            else:
                profit = prices[i] - cheapest
                max_profit = profit if profit > max_profit else max_profit

        return max_profit