from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.Helper(nums,k) - self.Helper(nums,k-1)

    def Helper(self,nums,p):
        dic=defaultdict(int)
        l=0
        r=0
        count=0
        n=len(nums)
        while(r<n):
            dic[nums[r]]+=1
            while len(dic)>p:
                dic[nums[l]]-=1
                if dic[nums[l]]==0:
                    dic.pop(nums[l])
                l+=1
            count+=(r-l+1)
            r+=1
        return count