class Solution:
    def func(self,idx,target):
        if target==0: return 1
        if idx==0:
            if target % self.coins[idx]==0: return 1
            else: return 0
        if self.dp[idx][target]!=-1: return self.dp[idx][target]
        not_take=self.func(idx-1,target)
        take=0
        if self.coins[idx]<=target:
            take=self.func(idx,target-self.coins[idx])
        self.dp[idx][target]=take+not_take
        return self.dp[idx][target]
    def change(self, amount: int, coins: List[int]) -> int:
        #n=len(coins)
        #self.coins=coins
        #self.dp=[[-1]*(amount+1) for _ in range(n)]
        #return self.func(n-1,amount)
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n)]
        for idx in range(n):
            dp[idx][0]=1
        for target in range(amount+1):
            if target % coins[0]==0:
                dp[0][target]=1
        for i in range(1,n):
            for target in range(1,amount+1):
                not_take=dp[i-1][target]
                take=0
                if coins[i]<=target:
                    take=dp[i][target-coins[i]]
                dp[i][target]=take+not_take
        return dp[n-1][amount]
        '''n=len(coins)
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
        return prev[amount]'''
        