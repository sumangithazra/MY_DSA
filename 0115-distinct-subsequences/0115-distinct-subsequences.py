class Solution:
    def func(self,i,j):
        if j==0: return 1
        if i==0 and j>0: return 0
        if self.dp[i][j]!=-1: return self.dp[i][j]
        if self.s[i-1]==self.t[j-1]:
            take=self.func(i-1,j-1)
            not_take=self.func(i-1,j)
            self.dp[i][j]= take+not_take
            return self.dp[i][j]
        else:
            self.dp[i][j]= self.func(i-1,j)
            return self.dp[i][j]

    def numDistinct(self, s: str, t: str) -> int:
        self.s=s
        self.t=t
        n=len(s)
        m=len(t)
        self.dp=[[-1]*(m+1) for _ in range(n+1)]
        return self.func(n,m)

        