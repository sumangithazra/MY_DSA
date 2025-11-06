class Solution:
    def func(self,i,j):
        if i>j: return 0
        if self.dp[i][j]!=-1: return self.dp[i][j]
        maxi=-1e9
        for k in range(i,j+1):
            cost=self.nums[i-1]*self.nums[k]*self.nums[j+1]+ self.func(i,k-1) + self.func(k+1,j)
            maxi=max(maxi,cost)
        self.dp[i][j]=maxi
        return self.dp[i][j]
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        #self.nums=nums
        #self.nums=[1]+self.nums +[1]
        #self.dp=[[-1]*(n+2) for _ in range(n+2)]
        #return self.func(1,n)
        nums=[1]+nums+[1]
        dp=[[0]*(n+2) for _ in range(n+2)]
        for i in range(n,0,-1):
            for j in range(i,n+1):
                maxi=-1e9
                for k in range(i,j+1):
                    cost=nums[i-1]*nums[k]*nums[j+1]+ dp[i][k-1] + dp[k+1][j]
                    maxi=max(maxi,cost)
                dp[i][j]=maxi
        return dp[1][n]
