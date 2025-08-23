from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        dictionary=Counter(nums)
        bucket=[0 for _ in range(n+1)]
        for item, val in dictionary.items():
            if bucket[val]==0:
                bucket[val]=[item]
            else: bucket[val].append(item)
        result=[]
        for i in range(n,0,-1):
            if bucket[i]!=0:
                result.extend(bucket[i])
            if len(result)==k:
                return result
        return result
        