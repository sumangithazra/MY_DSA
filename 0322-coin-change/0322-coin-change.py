class Solution:
    def func(self,idx,target):
        if target==0: return 0
        if idx==0:
            if target % self.coins[idx]==0: return target // self.coins[idx]
            else:
                return 1e9
        if self.dp[idx][target]!=-1: return self.dp[idx][target]
        not_take=self.func(idx-1,target)
        take=1e9
        if self.coins[idx]<=target:
            take=1+self.func(idx,target-self.coins[idx])
        self.dp[idx][target]=min(take,not_take)
        return self.dp[idx][target]
    def coinChange(self, coins: List[int], amount: int) -> int:
        #n=len(coins)
        #self.coins=coins
        #self.dp=[[-1]*(amount+1) for _ in range(n)]
        #ans=self.func(n-1,amount)
        #return -1 if ans==1e9 else ans
        n=len(coins)
        dp=[[1e9]*(amount+1) for _ in range(n)]
        for idx in range(n):
            dp[idx][0]=0
        for target in range(1,amount+1):
            if target % coins[0] ==0:
                dp[0][target]=target//coins[0]
        for i in range(1,n):
            for target in range(1,amount+1):
                not_take=dp[i-1][target]
                take=1e9
                if coins[i]<=target:
                    take=1+dp[i][target-coins[i]]
                dp[i][target]=min(take,not_take)
        ans=dp[n-1][amount]
        return -1 if ans==1e9 else ans



        