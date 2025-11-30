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
        #self.s=s
        #self.p=p
        #n=len(s)
        #m=len(p)
        #self.dp=[[-1]*(m+1) for _ in range(n+1)]
        #return self.func(n,m)
        '''n=len(s)
        m=len(p)
        dp=[[False]*(m+1) for _ in range(n+1)]
        dp[0][0]=True
        j=1
        while j<=m:
            if p[j-1]=='*':
                dp[0][j]=dp[0][j-1]
            else:
                dp[0][j]=False
            j+=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]= dp[i-1][j] or dp[i][j-1]
        return dp[n][m]'''
        n=len(s)
        m=len(p)
        prev=[False]*(m+1)
        curr=[False]*(m+1)
        prev[0]=True
        j=1
        while j<=m:
            if p[j-1]=='*':
                prev[j]=prev[j-1]
            else:
                prev[j]=False
            j+=1
        for i in range(1,n+1):
            curr[0]=False
            for j in range(1,m+1):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    curr[j]=prev[j-1]
                elif p[j-1]=='*':
                    curr[j]= prev[j] or curr[j-1]
                else:
                    curr[j]=False
            prev=curr[:]
        return prev[m]
        
        