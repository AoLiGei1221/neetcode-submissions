class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = [0] * n
        min_buy = prices[0]
        for i in range(1, n):
            min_buy = min(prices[i], min_buy)
            profit = prices[i] - min_buy
            ans[i] = max(ans[i-1], profit)
        
        return ans[n-1]

        