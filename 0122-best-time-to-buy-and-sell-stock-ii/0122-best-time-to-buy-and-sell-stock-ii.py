class Solution:
    def func(self,idx,buy):
        if idx==self.n: return 0
        if buy:
            return max(-self.prices[idx]+ self.func(idx+1,0), self.func(idx+1,1))
        else:
            return max(self.prices[idx]+self.func(idx+1,1), self.func(idx+1,0))
    def maxProfit(self, prices: List[int]) -> int:
        self.prices=prices
        #self.n=len(prices)
        #return self.func(0,1)
        n=len(prices)
        dp=[[0]*2 for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for buy in range(2):
                if buy:
                    dp[i][buy]=max(-prices[i]+dp[i+1][0], dp[i+1][1])
                else:
                    dp[i][buy]=max(prices[i]+dp[i+1][1],dp[i+1][0])
        return dp[0][1]
        
        