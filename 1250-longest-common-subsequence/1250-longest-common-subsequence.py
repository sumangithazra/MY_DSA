class Solution:
    def func(self,idx1,idx2):
        if idx1==0 or idx2==0 : return 0
        if self.s[idx1-1]==self.t[idx2-1]: return 1+ self.func(idx1-1,idx2-1)
        return max(self.func(idx1-1,idx2), self.func(idx1,idx2-1))
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.s=text1
        self.t=text2
        n=len(self.s)
        m=len(self.t)
        #return self.func(n,m)
        dp=[[-1]*(m+1) for i in range(n+1)]
        for i in range(n+1): dp[i][0]=0
        for j in range(m+1): dp[0][j]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if self.s[i-1]==self.t[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]