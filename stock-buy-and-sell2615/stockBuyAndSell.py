class Solution:
    def maximumProfit(self, prices) -> int:
        profit = 0
        n = len(prices)
        i = 0
        buy = 0
        brought_price = 0
        while i+1<n:
            if prices[i]>prices[i+1] and buy==1:
                profit += prices[i]-brought_price
                buy = 0
            elif prices[i]<prices[i+1] and buy==0:
                brought_price = prices[i]
                buy = 1
            i+=1
        if buy==1:
            profit += prices[i]-brought_price
        return profit
