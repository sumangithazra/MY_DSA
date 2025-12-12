class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumi=0
        maxi=-float('inf')
        for i in range(len(nums)):
            sumi+=nums[i]
            if sumi>maxi:
                maxi=sumi
            if sumi<0:
                sumi=0
        return maxi
        