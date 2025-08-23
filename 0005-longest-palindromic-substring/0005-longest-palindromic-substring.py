class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        leng=0
        for i in range(len(s)):
            #for odd length
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>leng:
                    res=s[l:r+1]
                    leng=r-l+1
                r+=1
                l-=1
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>leng:
                    res=s[l:r+1]
                    leng=r-l+1
                r+=1
                l-=1
        return res

        