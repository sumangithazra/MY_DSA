class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        curr=[1]*n
        maxi=1
        for idx in range(n):
            for pidx in range(idx):
                if nums[idx]>nums[pidx] and 1+dp[pidx]>dp[idx]:
                    dp[idx]=1+dp[pidx]
                    curr[idx]=curr[pidx] 
                elif nums[idx]>nums[pidx] and 1+dp[pidx]==dp[idx]:
                    curr[idx]+=curr[pidx]
            if dp[idx]>maxi:
                maxi=dp[idx]
        ans=0
        for i in range(n):
            if dp[i]==maxi:
                ans+=curr[i]
        return ans

            