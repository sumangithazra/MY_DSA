class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        r=""
        for i in range(n):
            if s[i].isalnum():
                r+=s[i]
        r=r.lower()
        return r==r[::-1]


        