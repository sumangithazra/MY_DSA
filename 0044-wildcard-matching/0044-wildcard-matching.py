class Solution:
    def func(self,i,j):
        if i==0 and j==0: return True
        if i==0 and j>0:
            while j>0:
                if self.p[j-1]!='*':
                    return False
                j-=1
            return True
        if j==0: return False
        if self.dp[i][j]!=-1: return self.dp[i][j]

        if self.p[j-1]=='?' or self.s[i-1]==self.p[j-1]:
            self.dp[i][j]= self.func(i-1,j-1)
            return self.dp[i][j]
        elif self.p[j-1]=='*':
            self.dp[i][j]= self.func(i,j-1) or self.func(i-1,j)
            return self.dp[i][j]
        else: return False
    def isMatch(self, s: str, p: str) -> bool:
        self.s=s
        self.p=p
        n=len(s)
        m=len(p)
        self.dp=[[-1]*(m+1) for _ in range(n+1)]
        return self.func(n,m)
        