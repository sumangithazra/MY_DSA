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
        #dp=[[False]*(sumi+1) for _ in range(self.n)]
        prev=[False]*(sumi+1)
        curr=[False]*(sumi+1)
        
        #for idx in range(self.n):
            #dp[idx][0]=True
        prev[0]=True
        if self.nums[0]<=sumi:
            prev[self.nums[0]]=True
        for idx in range(1,self.n):
            #curr=[False]*(sumi+1)
            curr[0]=True
            for target in range(1,sumi+1):
                not_take=prev[target]
                take=False
                if self.nums[idx]<=target:
                    take=prev[target-self.nums[idx]]
                curr[target]=take or not_take
            prev=curr[:]
        return prev[sumi]


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