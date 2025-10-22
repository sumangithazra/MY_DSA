import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2: return 0
    
        arr=[1]*(n+1)
        arr[0]=0
        arr[1]=0
        for i in range(2,int(math.sqrt(n))+1):
            if arr[i]==1:
                for j in range(i*i,n+1,i):
                    arr[j]=0
        ans=[]
        for i in range(2,n):
            if arr[i]==1:
                ans.append(i)
        return len(ans)
                
        