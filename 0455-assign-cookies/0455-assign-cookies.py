class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        '''m=len(g)
        n=len(s)
        g.sort()
        s.sort()
        l=0
        r=0
        while l<n:
            if r<m and g[r]<=s[l]:
                r+=1
            l+=1
        return r'''
        m=len(g)
        n=len(s)
        s.sort()
        g.sort()
        l,r=0,0
        while l<n and r<m:
            if g[r]<=s[l]:
                r+=1
            l+=1
        return r

        
        