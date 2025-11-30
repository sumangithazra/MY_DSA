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
        n=len(s)
        self.s=s
        self.t=s[::-1]
        self.dp=[[-1]*(n+1) for _ in range(n+1)]
        return n-self.func(n,n)

        