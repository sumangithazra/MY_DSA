class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=float('inf')
        left=0
        Sum=0
        for right in range(len(nums)):
            Sum+=nums[right]
            while Sum>=target:
                mini=min(mini,right-left+1)
                Sum-=nums[left]
                left+=1
        return mini if mini!=float('inf') else 0


            

        