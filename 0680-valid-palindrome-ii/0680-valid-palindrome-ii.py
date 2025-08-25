class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]: return True
        n=len(s)
        i=0
        j=n-1
        count=0
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                if s[i]!=s[j] and count==0:
                    p=s[:i]+s[i+1:]
                    q=s[:j]+s[j+1:]
                    if p==p[::-1]: return True 
                    elif q==q[::-1]: return True
                    count+=1
                else: return False
        return True
        