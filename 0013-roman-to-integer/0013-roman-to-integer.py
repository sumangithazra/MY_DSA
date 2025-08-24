class Solution:
    def romanToInt(self, s: str) -> int:
        '''mpp={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev=0
        total=0
        for ch in reversed(s):
            crr_val=mpp[ch]
            if crr_val<prev: total-=crr_val
            else:
                total+=crr_val
                prev=crr_val
        return total'''
        r_to_int={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total=0
        i=len(s)-1
        while i>=0:
            if i>0 and r_to_int[s[i]]>r_to_int[s[i-1]]:
                total+=r_to_int[s[i]]-r_to_int[s[i-1]]
                i-=2
            else:
                total+=r_to_int[s[i]]
                i-=1
        return total

        