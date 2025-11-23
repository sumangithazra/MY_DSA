class Solution:
    def func(self,i,j,dp):
        if i==0 and j>=0 and j<self.n: return self.matrix[i][j]
        if dp[i][j]!=-1: return dp[i][j]
        up=self.matrix[i][j]+ self.func(i-1,j,dp)
        left_d=1e9
        if j-1>=0: left_d=self.matrix[i][j]+ self.func(i-1,j-1,dp)
        right_d=1e9
        if j+1<self.n: right_d=self.matrix[i][j]+ self.func(i-1,j+1,dp)
        dp[i][j]=min(up,left_d,right_d)
        return dp[i][j]
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #self.n=len(matrix)
        #self.matrix=matrix
        #mini=1e9
        #for j in range(self.n):
            #dp=[[-1]*self.n for _ in range(self.n)]
            #mini=min(mini,self.func(self.n-1,j,dp))
        #return mini
        n=len(matrix)
        dp=[[0]*n for _ in range(n)]
        for i in range(n):
            dp[0][i]=matrix[0][i]
        for i in range(1,n):
            for j in range(n):
                up=matrix[i][j]+ dp[i-1][j]
                left_d=1e9
                right_d=1e9
                if j-1>=0:
                    left_d=matrix[i][j] + dp[i-1][j-1]
                if j+1<n:
                    right_d=matrix[i][j]+ dp[i-1][j+1]
                dp[i][j]=min(up,left_d,right_d)
        mini=1e9
        for j in range(n):
            mini=min(mini,dp[n-1][j])
        return mini
        '''n=len(matrix)
        dp=[[-1]*n for _ in range(n)]
        for col in range(n):
            dp[0][col]=matrix[0][col]

        for row in range(1,n):
            for col in range(n):
                ld=1e9
                rd=1e9
                up=matrix[row][col]+dp[row-1][col]
                if col-1>=0 : ld=matrix[row][col]+dp[row-1][col-1]
                if col+1<n : rd=matrix[row][col]+dp[row-1][col+1]
                dp[row][col]=min(up,ld,rd)
        mini=dp[n-1][0]
        for col in range(1,n):
            mini=min(mini,dp[n-1][col])
        return mini'''
        n=len(matrix)
        prev=[0]*n
        curr=[0]*n
        for col in range(n):
            prev[col]=matrix[0][col]

        for row in range(1,n):
            for col in range(n):
                ld=1e9
                rd=1e9
                up=matrix[row][col]+prev[col]
                if col-1>=0 : ld=matrix[row][col]+prev[col-1]
                if col+1<n : rd=matrix[row][col]+prev[col+1]
                curr[col]=min(up,ld,rd)
            prev=curr[:]
        mini=prev[0]
        for col in range(1,n):
            mini=min(mini,prev[col])
        return mini
        