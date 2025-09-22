from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''count=0
        pfx_sum=0
        sum_mpp={0:1}
        for num in nums:
            pfx_sum+=num
            if (pfx_sum-k) in sum_mpp:
                count+=sum_mpp[pfx_sum-k]
            sum_mpp[pfx_sum]=sum_mpp.get(pfx_sum,0)+1
        return count '''  
        dictionary=defaultdict(int)
        count=0
        pre_sum=0
        dictionary[pre_sum]=1
        for num in nums:
            pre_sum+=num
            if pre_sum-k in dictionary:
                count+=dictionary[pre_sum-k]
            dictionary[pre_sum]+=1
        return count    