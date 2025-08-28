class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        l=0
        r=0
        farthest=0
        jumps=0
        while r<n-1:
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            jumps+=1
            l=r+1
            r=farthest
        return jumps


        