class Solution:
    def func(self,i,j):
        if i==0 or j==0: return 0
        if self.dp[i][j]!=-1: return self.dp[i][j]
        if self.text1[i-1]==self.text2[j-1]: 
            self.dp[i][j]=1+ self.func(i-1,j-1)
            return self.dp[i][j]
        else: 
            self.dp[i][j]= max(self.func(i-1,j),self.func(i,j-1))
            return self.dp[i][j]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.text1=text1
        self.text2=text2
        n=len(text1)
        m=len(text2)
        self.dp=[[-1]*(m+1) for _ in range(n+1)]
        return self.func(n,m)


