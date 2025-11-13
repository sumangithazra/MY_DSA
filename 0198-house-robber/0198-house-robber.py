class Solution:
    def func(self,i):
        if i==0: return self.nums[i]
        if i<0: return 0
        if self.dp[i]!=-1: return self.dp[i]
        not_take=self.func(i-1)
        take=0
        if i>=1:
            take=self.nums[i]+self.func(i-2)
        self.dp[i]=max(take,not_take)
        return self.dp[i]
    def rob(self, nums: List[int]) -> int:
        #self.nums=nums
        #self.dp=[-1]*(len(nums)+1)
        #return self.func(len(nums)-1)
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        for i in range(1,n):
            not_take=dp[i-1]
            take=nums[i]
            if i>1:
                take+=dp[i-2]
            dp[i]=max(take,not_take)
        return dp[n-1]

        '''prev=nums[0]
        prev2=0
        for i in range(1,len(nums)):
            take=nums[i]
            if i>1: take+=prev2
            non_take=prev
            curr=max(take,non_take)

            prev2=prev
            prev=curr
        return prev'''
        
        