class Solution:
    def func(self,i,j):
        if i>j: return 0
        mini=1e9
        for k in range(i,j+1):
            cost=self.cuts[j+1]-self.cuts[i-1]+self.func(i,k-1)+self.func(k+1,j)
            mini=min(mini,cost)
        return mini
    def minCost(self, n: int, cuts: List[int]) -> int:
        self.cuts=cuts
        self.cuts.sort()
        self.cuts.insert(0,0)
        self.cuts.append(n)
        #return self.func(1,len(self.cuts)-2)
        m=len(self.cuts)
        dp=[[0]*(m) for i in range(m)]
        for i in range(m-2,0,-1):
            for j in range(i,m-1):
                mini=1e9
                for k in range(i,j+1):
                   cost=self.cuts[j+1]-self.cuts[i-1]+dp[i][k-1]+dp[k+1][j]
                   mini=min(mini,cost)
                dp[i][j]=mini
        return dp[1][m-2]

        