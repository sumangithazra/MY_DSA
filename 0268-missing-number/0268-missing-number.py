class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''n=len(nums)
        sum=(n*(n+1))/2
        for i in range(n):
            sum-=nums[i]
        return int(sum)'''
        xor=0
        for i in range(len(nums)):
            xor=xor^nums[i]
        for i in range(len(nums)+1):
            xor=xor^i
        return xor
        