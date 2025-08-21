class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==divisor: return 1
        result=0
        sign=True
        if dividend>=0 and divisor<0: sign=False
        if dividend<0 and divisor>0: sign=False
        n=abs(dividend)
        d=abs(divisor)
        while n>=d:
            count=0
            while n>= d<<count+1:
                count+=1
            result+=1<<count
            n-=d<<count
        if result> 2**31 -1 and sign==True: return 2**31 -1
        if result>2**31 and sign==False: return -2**31
        return result if sign else -result

        