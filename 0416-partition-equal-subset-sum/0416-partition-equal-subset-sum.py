class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum=0
        for i in range(len(nums)):
            total_sum+=nums[i]
        if total_sum%2==1: return False
        return self.sub_sum_k(nums,total_sum//2)
    def sub_sum_k(self,nums,k):
        n=len(nums)
        dp=[[False]*(k+1) for _ in range(n)]
        for i in range(n):
            dp[i][0]=True
        if nums[0]<=k: dp[0][nums[0]]=True
        for idx in range(1,n):
            for target in range(1,k+1):
                not_take=dp[idx-1][target]
                take=False
                if nums[idx]<=target:
                    take=dp[idx-1][target-nums[idx]]
                dp[idx][target]=not_take or take
        return dp[n-1][k]
        