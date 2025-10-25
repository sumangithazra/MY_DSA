class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''if amount==0: return 0
        coins.sort()
        n=len(coins)
        count=0
        for i in range(n-1,-1,-1):
            while amount>=coins[i]:
                count+=1
                amount-=coins[i]
        if amount!=0: return -1
        return count'''
        n=len(coins)
        dp=[[1e9]*(amount+1) for _ in range(n)]
        for i in range(amount+1):
            if i%coins[0]==0: dp[0][i]=i//coins[0]
        for idx in range(1,n):
            for target in range(amount+1):
                not_take=0+dp[idx-1][target]
                take=1e9
                if coins[idx]<=target:
                    take=1+dp[idx][target-coins[idx]]
                dp[idx][target]=min(take,not_take)
        ans=dp[n-1][amount]
        return -1 if ans>=1e9 else ans


        