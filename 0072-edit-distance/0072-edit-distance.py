class Solution:
    def func(self,i,j):
        if i==0: return j
        if j==0: return i
        if self.dp[i][j]!=-1: return self.dp[i][j]

        if self.word1[i-1]==self.word2[j-1]:
            self.dp[i][j]= self.func(i-1,j-1)
            return self.dp[i][j]
        else:
            insert=1+self.func(i,j-1)
            delete=1+self.func(i-1,j)
            replace=1+ self.func(i-1,j-1)
            self.dp[i][j]= min(insert,delete, replace)
            return self.dp[i][j]
    def minDistance(self, word1: str, word2: str) -> int:
        #self.word1=word1
        #self.word2=word2
        #n=len(word1)
        #m=len(word2)
        #self.dp=[[-1]*(m+1) for _ in range(n+1)]
        #return self.func(n,m)
        '''n=len(word1)
        m=len(word2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=i
        for j in range(m+1):
            dp[0][j]=j
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    insert=1+dp[i][j-1]
                    delete=1+dp[i-1][j]
                    replace=1+dp[i-1][j-1]
                    dp[i][j]=min(insert, delete, replace)
        return dp[n][m]'''
        n=len(word1)
        m=len(word2)
        prev=[0]*(m+1)
        curr=[0]*(m+1)
        for j in range(m+1):
            prev[j]=j
        for i in range(1,n+1):
            curr[0]=i
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    curr[j]=prev[j-1]
                else:
                    insert=1+curr[j-1]
                    delete=1+prev[j]
                    replace=1+prev[j-1]
                    curr[j]=min(insert, delete, replace)
            prev=curr[:]
        return prev[m]