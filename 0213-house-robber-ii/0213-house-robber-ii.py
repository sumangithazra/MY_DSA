class Solution:
    def func(self,i,nums,dp):
        if i==0: return nums[i]
        if i<0: return 0
        if dp[i]!=-1: return dp[i]
        not_take=self.func(i-1,nums,dp)
        take=nums[i]+self.func(i-2,nums,dp)
        dp[i]=max(take,not_take)
        return dp[i]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if len(nums)==0: return 0
        if len(nums)==1: return nums[0]
        temp1=nums[:n-1]
        temp2=nums[1:n]
        #dp1=[-1]*(len(temp1))
        #dp2=[-1]*(len(temp2))
        #return max(self.func(len(temp1)-1,temp1,dp1),self.func(len(temp2)-1,temp2,dp2))
        return max(self.Helper(temp1),self.Helper(temp2))
    def Helper(self,arr):
        n=len(arr)
        dp=[0]*n
        dp[0]=arr[0]
        for i in range (1,n):
            not_take=dp[i-1]
            take=arr[i]
            if i-2>=0:
                take+=dp[i-2]
            dp[i]=max(take,not_take)
        return dp[n-1]
        