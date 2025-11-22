class Solution:
    def func(self,i,j):
        if self.obstacleGrid[i][j]==1: return 0
        if i==0 and j==0: return 1
        if i<0 or j<0 : return 0
        if self.dp[i][j]!=-1: return self.dp[i][j]
        up=self.func(i-1,j)
        left=self.func(i,j-1)
        self.dp[i][j]=up+left
        return self.dp[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #self.obstacleGrid=obstacleGrid
        #m=len(self.obstacleGrid)
        #n=len(self.obstacleGrid[0])
        #self.dp=[[-1]*n for _ in range(m)]
        #return self.func(m-1,n-1)
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                elif i==0 and j==0:
                    dp[i][j]=1
                else:
                    up=0
                    left=0
                    if i>0: up=dp[i-1][j]
                    if j>0: left=dp[i][j-1]
                    dp[i][j]=up+left
        return dp[m-1][n-1]

        '''m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        #dp=[[-1]*n for _ in range(m)]
        prev=[0]*n
        for i in range(m):
            curr=[0]*n
            for j in range(n):
                if obstacleGrid[i][j]==1: curr[j]=0
                elif i==0 and j==0: curr[j]=1
                else:
                    up=0
                    left=0
                    if i>0: up=prev[j]
                    if j>0: left=curr[j-1]
                    curr[j]=up+left
            prev=curr
        return prev[n-1]'''

        