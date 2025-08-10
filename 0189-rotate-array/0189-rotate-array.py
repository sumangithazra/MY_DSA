class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #n = len(nums)
        #k %= n  # Ensure k is within the array length
        #nums[:] = nums[-k:] + nums[:-k]
        n=len(nums)
        k%=n
        nums[:]=list(reversed(nums[:n-k]))+list(reversed(nums[n-k:]))
        return nums.reverse()



