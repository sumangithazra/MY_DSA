class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''max_profit=0
        mini=prices[0]
        for i in range(1,len(prices)):
            profit=prices[i]-mini
            max_profit=max(max_profit,profit)
            mini=min(mini,prices[i])
        return max_profit'''
        profit=0
        mini=prices[0]
        n=len(prices)
        for i in range(1,n):
            profit=max(profit,prices[i]-mini)
            mini=min(mini,prices[i])
        return profit

        