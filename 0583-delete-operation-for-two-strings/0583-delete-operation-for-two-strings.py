class Solution:
    def func(self,i,j):
        if i==0 or j==0: return 0
        if self.dp[i][j]!=-1: return self.dp[i][j]
        if self.word1[i-1]==self.word2[j-1]:
            self.dp[i][j]= 1+self.func(i-1,j-1)
            return self.dp[i][j]
        else:
            self.dp[i][j]= max(self.func(i-1,j),self.func(i,j-1))
            return self.dp[i][j]
    def minDistance(self, word1: str, word2: str) -> int:
        self.word1=word1
        self.word2=word2
        n=len(word1)
        m=len(word2)
        self.dp=[[-1]*(m+1) for _ in range(n+1)]
        return (m+n)- 2*self.func(n,m)
        