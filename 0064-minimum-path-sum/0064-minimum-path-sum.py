class Solution:
    def func(self,i,j):
        if i==0 and j==0: return self.grid[i][j]
        if i<0 or j<0: return 1e9
        if self.dp[i][j]!=-1: return self.dp[i][j]
        up=self.grid[i][j]+ self.func(i-1,j)
        left=self.grid[i][j] + self.func(i,j-1)
        self.dp[i][j]=min(up,left)
        return self.dp[i][j]
    def minPathSum(self, grid: List[List[int]]) -> int:
        #self.grid=grid
        #m=len(grid)
        #n=len(grid[0])
        #self.dp=[[-1]*n for _ in range(m)]
        #return self.func(m-1,n-1)
        m=len(grid)
        n=len(grid[0])
        prev=[0]*n
        curr=[0]*n
        for i in range(m):
            for j in range(n):
                if i==0 and j==0: 
                    curr[j]=grid[0][0]
                    continue
                up=1e9
                left=1e9
                if i>0: up=grid[i][j]+ prev[j]
                if j>0: left=grid[i][j]+ curr[j-1]
                curr[j]=min(left,up)
            prev=curr[:]
        return prev[n-1]
        '''m=len(grid)
        n=len(grid[0])
        dp=[[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0: 
                    dp[i][j]=grid[i][j]
                    continue
                up=grid[i][j]
                if i>0: up+=dp[i-1][j]
                else:
                    up=1e9
                left=grid[i][j]
                if j>0: left+=dp[i][j-1]
                else: left=1e9
                dp[i][j]=min(up,left)
        return dp[m-1][n-1] '''
        