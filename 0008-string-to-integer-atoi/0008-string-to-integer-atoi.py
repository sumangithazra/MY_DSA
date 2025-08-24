class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        i=0
        int_max=2**31-1
        int_min=-2**31
        while i<n and s[i]==' ':
            i+=1
        if i==n: return 0
        sign=1
        if s[i]=='-':
            sign=-1
            i+=1
        elif s[i]=='+':
            i+=1
        result=0
        while i<n and s[i].isdigit():
            result=result*10 +int(s[i])
            if result*sign<=int_min: return int_min
            if result*sign>=int_max: return int_max
            i+=1
        return result*sign


        