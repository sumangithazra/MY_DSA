class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n)]
        for target in range(amount+1):
            dp[0][target]= 1 if target%coins[0]==0 else 0
        for idx in range(1,n):
            for target in range(amount+1):
                not_take=dp[idx-1][target]
                take=0
                if coins[idx]<=target:
                    take=dp[idx][target-coins[idx]]
                dp[idx][target]=take+not_take
        return dp[n-1][amount]'''
        n=len(coins)
        #dp=[[0]*(amount+1) for _ in range(n)]
        prev=[0]*(amount+1)
        curr=[0]*(amount+1)
        for target in range(amount+1):
            prev[target]= 1 if target%coins[0]==0 else 0
        for idx in range(1,n):
            for target in range(amount+1):
                not_take=prev[target]
                take=0
                if coins[idx]<=target:
                    take=curr[target-coins[idx]]
                curr[target]=take+not_take
            prev=curr[:]
        return prev[amount]
        