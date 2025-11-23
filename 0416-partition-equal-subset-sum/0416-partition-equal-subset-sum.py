class Solution:
    def func(self,idx,target):
        if target==0: return True
        if idx==0: return self.nums[idx]==target
        if self.dp[idx][target]!=False: return self.dp[idx][target]
        not_take=self.func(idx-1,target)
        take=False
        if self.nums[idx]<=target:
            take=self.func(idx-1,target-self.nums[idx])
        self.dp[idx][target]=take or not_take
        return self.dp[idx][target]
    def CheckSum(self,sumi):
        dp=[[False]*(sumi+1) for _ in range(self.n)]
        for idx in range(self.n):
            dp[idx][0]=True
        if self.nums[0]<=sumi:
            dp[0][self.nums[0]]=True
        for idx in range(self.n):
            for target in range(1,sumi+1):
                not_take=dp[idx-1][target]
                take=False
                if self.nums[idx]<=target:
                    take=dp[idx-1][target-self.nums[idx]]
                dp[idx][target]=take or not_take
        return dp[self.n-1][sumi]


    def canPartition(self, nums: List[int]) -> bool:
        self.nums=nums
        #n=len(nums)
        self.n=len(nums)
        sumi=0
        
        for i in self.nums:
            sumi+=i
        if sumi%2==1: return False
        #self.dp=[[False]*(sumi//2 +1) for _ in range(n)]
        #return self.func(n-1,sumi//2)
        return self.CheckSum(sumi//2)