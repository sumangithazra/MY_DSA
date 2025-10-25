class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''total=sum(nums)
        if total<abs(target) or (total+target)%2!=0: return 0
        n=len(nums)
        s=(total+target)//2
        dp=[[0]*(s+1) for _ in range(n)]
        if nums[0]==0:
            dp[0][0]=2
        else:
            dp[0][0]=1
            if nums[0]<=s: dp[0][nums[0]]=1
        for idx in range(1,n):
            for trg in range(s+1):
                not_take=dp[idx-1][trg]
                take=0
                if nums[idx]<=trg:
                    take=dp[idx-1][trg-nums[idx]]
                dp[idx][trg]=not_take+take
        return dp[n-1][s]'''
        total=sum(nums)
        if total<abs(target) or (total+target)%2!=0: return 0
        n=len(nums)
        s=(total+target)//2
        #dp=[[0]*(s+1) for _ in range(n)]
        prev=[0]*(s+1)
        curr=[0]*(s+1)
        if nums[0]==0:
            prev[0]=2
        else:
            prev[0]=1
            if nums[0]<=s: prev[nums[0]]=1
        for idx in range(1,n):
            for trg in range(s+1):
                not_take=prev[trg]
                take=0
                if nums[idx]<=trg:
                    take=prev[trg-nums[idx]]
                curr[trg]=not_take+take
            prev=curr[:]
        return prev[s]
        
        