class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        temp1=nums[:len(nums)-1]
        temp2=nums[1:]
        return max(self.Finding_max(temp1),self.Finding_max(temp2))
    
    def Finding_max(self,var):
        prev=var[0]
        prev2=0
        for i in range(1,len(var)):
            take=var[i]
            if i>1: take+=prev2
            non_take=prev
            curr=max(take,non_take)
            prev2=prev
            prev=curr
        return prev

        