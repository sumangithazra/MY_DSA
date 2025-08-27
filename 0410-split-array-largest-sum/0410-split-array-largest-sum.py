class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=low+(high-low)//2
            total_partetion=self.partetion_count(nums,mid)
            if total_partetion<=k:
                high=mid-1
            else:
                low=mid+1
        return low
    def partetion_count(self,nums,mid):
        count=1
        total_sum=0
        for i in range(len(nums)):
            if total_sum+nums[i]<=mid:
                total_sum+=nums[i]
            else:
                count+=1
                total_sum=nums[i]
        return count
        