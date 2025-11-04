class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        maxi=1
        for idx in range(n):
            for pidx in range(idx):
                if nums[idx]>nums[pidx]:
                    dp[idx]=max(1+dp[pidx],dp[idx])
            maxi=max(maxi,dp[idx])
        return maxi        