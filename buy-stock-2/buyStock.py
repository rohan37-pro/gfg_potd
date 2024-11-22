class Solution:
    def maximumProfit(self, prices):
        n = len(prices)
        if n==0:
            return 0
        i = 1
        small = prices[0]
        profit = 0
        while i<n:
            if small<prices[i] and profit<prices[i]-small:
                profit = prices[i]-small
            if small>prices[i] :
                small = prices[i]
            i+=1
        return profit
        