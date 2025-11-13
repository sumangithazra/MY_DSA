class Solution:
    def func(self,i):
        if i==1: return 1
        if i==2: return 2
        if self.dp[i]!=-1: return self.dp[i]
        step1=self.func(i-1)
        step2=0
        if i>=2:
            step2=self.func(i-2)
        self.dp[i]=step1+step2
        return self.dp[i]
    def climbStairs(self, n: int) -> int:
        self.dp=[-1]*(n+1)
        '''if n==1:
            return 1
        elif n==2:
            return 2
        last=2
        second_last=1
        for i in range(3,n+1):
            new=last+second_last
            last,second_last=new,last
        return new'''
        return self.func(n)
