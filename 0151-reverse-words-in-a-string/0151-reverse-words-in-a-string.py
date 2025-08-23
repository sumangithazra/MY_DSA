class Solution:
    def reverseWords(self, s: str) -> str:
        y=s.split()
        x=y[::-1]
        ans=" ".join(x)
        return ans 
        