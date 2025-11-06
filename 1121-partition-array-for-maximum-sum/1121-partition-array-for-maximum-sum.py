class Solution:
    def func(self,i):
        if i==self.n: return 0
        if self.dp[i]!=-1: return self.dp[i]
        maxi=-1e9
        max_arr=0
        for j in range(i,min(i+self.k,self.n)):
            max_arr=max(max_arr,self.arr[j])
            cost=(max_arr*(j-i+1))+ self.func(j+1)
            maxi=max(maxi,cost)
        self.dp[i]=maxi
        return self.dp[i]


    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        #self.arr=arr
        #self.k=k
        #self.n=len(arr)
        #self.dp=[-1]*(self.n)
        #return self.func(0)
        n=len(arr)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            maxi=-1e9
            max_arr=0
            for j in range(i,min(i+k,n)):
                max_arr=max(max_arr,arr[j])
                cost=(max_arr*(j-i+1))+ dp[j+1]
                maxi=max(maxi,cost)
            dp[i]=maxi
        return dp[0]
            
        