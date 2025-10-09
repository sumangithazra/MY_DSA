class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        dp[0]=nums[0]
        for i in range(1,n):
            take=nums[i]
            if i>1: take+=dp[i-2]
            non_take=dp[i-1]
            dp[i]=max(take,non_take)
        return dp[n-1]
        