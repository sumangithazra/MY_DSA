from collections import defaultdict
class Solution:
    def beautySum(self, s: str) -> int:
        n=len(s)
        total_beauty=0
        
        for i in range(n):
            #max_freq=1
            #min_freq=1
            dictionary=defaultdict(int)
            for j in range(i,n):
                dictionary[s[j]]+=1
                max_freq=max(dictionary.values())
                min_freq=min(dictionary.values())
                total_beauty+=max_freq-min_freq
        return total_beauty


        