class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m=200
        count=0
        flag=0
        for i in strs:
            m=min(m,len(i))
        for i in range(m):
            ans=strs[0][i]
            for j in strs:
                if j[i]!=ans:
                    flag=1
            if flag==1:
                break
            count+=1  
        return strs[0][:count] 

        