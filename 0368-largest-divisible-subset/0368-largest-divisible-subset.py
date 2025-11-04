class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dp=[1]*n
        nums.sort()
        maxi=1
        last_idx=0
        hashm=[i for i in range(n)]
        for idx in range(n):
            for pidx in range(idx):
                if nums[idx] % nums[pidx]==0 and 1+dp[pidx]>dp[idx]:
                    dp[idx]=dp[pidx]+1
                    hashm[idx]=pidx


            if dp[idx]>maxi:
                maxi=dp[idx]
                last_idx=idx
        ans=[]
        ans.append(nums[last_idx])
        while hashm[last_idx]!=last_idx:
            last_idx=hashm[last_idx]
            ans.append(nums[last_idx])
        return ans[::-1]