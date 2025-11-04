class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        trasc=4
        dp=[[0]*(5) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for trasc in range(4):
                if trasc%2==0:
                    dp[i][trasc]=max(-prices[i]+dp[i+1][trasc+1], dp[i+1][trasc])
                else:
                    dp[i][trasc]=max(prices[i]+dp[i+1][trasc+1],dp[i+1][trasc])
        return dp[0][0]
        