class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''idx=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                idx=i
                break
        if idx==-1:
            nums[:]=nums[::-1]
        else:
            for i in range(len(nums)-1,idx,-1):
                if nums[idx]<nums[i]:
                    nums[idx], nums[i]=nums[i], nums[idx]
                    break
                    
            nums[:]=nums[:idx+1]+nums[-1:-(len(nums)-idx):-1]'''
        idx=-1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                idx=i
                break
        if idx==-1: nums.reverse()
        else:
            for i in range(n-1,idx,-1):
                if nums[i]>nums[idx]:
                    nums[i],nums[idx]=nums[idx],nums[i]
                    break
            nums[:]=nums[:idx+1]+nums[:-(n-idx):-1]

        