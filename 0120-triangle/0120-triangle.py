class Solution:
    def func(self,i,j):
        if i==self.m-1: return self.triangle[self.m-1][j]
        if self.dp[i][j]!=-1: return self.dp[i][j]
        down=self.triangle[i][j]+ self.func(i+1,j)
        right=self.triangle[i][j]+ self.func(i+1,j+1)
        self.dp[i][j]=min(down,right)
        return self.dp[i][j]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #m=len(triangle)
        #self.triangle=triangle
        #self.m=m
        #self.dp=[[-1]*m for _ in range(m)]
        #return self.func(0,0)
        m=len(triangle)
        dp=[[0]*m for _ in range(m)]
        for j in range(m):
            dp[m-1][j]=triangle[m-1][j]
        for i in range(m-2,-1,-1):
            for j in range(i,-1,-1):
                down=triangle[i][j]+ dp[i+1][j]
                right=triangle[i][j]+dp[i+1][j+1]
                dp[i][j]=min(down,right)
        return dp[0][0]
        '''n=len(triangle)
        dp=[[-1]*n for _ in range(n)]
        for j in range(n): dp[n-1][j]=triangle[n-1][j]
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                d=triangle[i][j]+ dp[i+1][j]
                dg=triangle[i][j] + dp[i+1][j+1]
                dp[i][j]=min(d,dg)
        return dp[0][0]'''
        