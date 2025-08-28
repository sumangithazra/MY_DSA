class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #if len(nums)==1:return True
        n=len(nums)
        max_idx=0
        for i in range(n):
            if i>max_idx: return False
            max_idx=max(max_idx,i+nums[i])
        if max_idx>=n-1: return True
        