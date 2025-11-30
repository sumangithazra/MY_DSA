class Solution:
    def func(self,i,j):
        if i==0 or j==0: return 0
        if self.dp[i][j]!=-1: return self.dp[i][j]
        if self.s[i-1]==self.t[j-1]:
            self.dp[i][j]= 1+ self.func(i-1,j-1)
            return self.dp[i][j]
        else:
            self.dp[i][j]= max(self.func(i-1,j),self.func(i,j-1))
            return self.dp[i][j]
    def minInsertions(self, s: str) -> int:
        #n=len(s)
        #self.s=s
        #self.t=s[::-1]
        #self.dp=[[-1]*(n+1) for _ in range(n+1)]
        #return n-self.func(n,n)
        n=len(s)
        t=s[::-1]
        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=1+ dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return n-dp[n][n]

        