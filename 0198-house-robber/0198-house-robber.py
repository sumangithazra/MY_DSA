class Solution:
    def rob(self, nums: List[int]) -> int:
        prev=nums[0]
        prev2=0
        for i in range(1,len(nums)):
            take=nums[i]
            if i>1: take+=prev2
            non_take=prev
            curr=max(take,non_take)

            prev2=prev
            prev=curr
        return prev
        
        