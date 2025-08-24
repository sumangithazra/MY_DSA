from collections import Counter
from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        '''count=Counter(s)
        bucket=defaultdict(list)
        max_freq=max(count.values())
        for item,cnt in count.items():
            bucket[cnt].append(item)
        res=[]
        for i in range(max_freq,0,-1):
            for ch in bucket[i]:
                res.append(ch*i)

        return ''.join(res)'''
        '''dictionary={}
        for i in range(len(s)):
            if s[i] in dictionary: 
                dictionary[s[i]]+=1
            else: dictionary[s[i]]=1
        sorted_dict=dict(sorted(dictionary.items(),key=lambda x:x[1],reverse=True))
        res=''
        for ch,cnt in sorted_dict.items():
            res+=ch*cnt
        return res'''
        dictionary=Counter(s)
        bucket=defaultdict(list)
        result=''
        max_freq=max(dictionary.values())
        for ch,freq in dictionary.items():
            bucket[freq].append(ch)
        for i in range(max_freq,0,-1):
            for ch in bucket[i]:
                result+=ch*i
        return result


        