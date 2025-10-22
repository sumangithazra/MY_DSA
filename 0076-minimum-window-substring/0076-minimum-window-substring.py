from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)
        if m==0 or n==0: return ""
        dic=defaultdict(int)
        Sindex=-1
        max_len=float('inf')
        l=0
        r=0
        count=0
        for i in range(m):
            dic[t[i]]+=1
        while r<n:
            if dic[s[r]]>0: count+=1
            dic[s[r]]-=1
            while count==m:
                if r-l+1<max_len:
                    max_len=r-l+1
                    Sindex=l
                dic[s[l]]+=1
                if dic[s[l]]>0: count-=1
                l+=1
            r+=1
        return "" if Sindex==-1 else s[Sindex:Sindex+max_len]

        