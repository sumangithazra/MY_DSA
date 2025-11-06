class Solution:
    def isPalindrom(self,t):
        i=0
        j=len(t)-1
        while i<j:
            if t[i]!=t[j]: return False
            i+=1
            j-=1
        return True
    def func(self,i):
        if i==self.n: return 0
        if self.dp[i]!=-1: return self.dp[i]
        mini=1e9
        for k in range(i,self.n):
            if self.isPalindrom(self.s[i:k+1]):
                cost=1+self.func(k+1)
                mini=min(mini,cost)
        self.dp[i]=mini
        return self.dp[i]

    def minCut(self, s: str) -> int:
        #self.s=s
        #self.n=len(self.s)
        #self.dp=[-1]*(self.n+1)
        #return self.func(0)-1
        n=len(s)
        dp=[0]*(n+1)
        def isPalindrom(t):
            i=0
            j=len(t)-1
            while i<j:
                if t[i]!=t[j]: return False
                i+=1
                j-=1
            return True
        pal=[[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or pal[i+1][j-1]):
                    pal[i][j]=True
        
        for i in range(n-1,-1,-1):
            mini=1e9
            for k in range(i,n):
                if pal[i][k]:
                    cost=1+dp[k+1]
                    mini=min(mini,cost)
            dp[i]=mini
        return dp[0]-1
            

