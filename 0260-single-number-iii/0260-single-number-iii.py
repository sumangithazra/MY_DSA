class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        for i in range(len(nums)):
            xor=xor^nums[i]
        rightmost_bit=(xor & (xor-1)) ^ xor
        bucket1=0
        bucket2=0
        for i in range(len(nums)):
            if nums[i] & rightmost_bit: bucket1=bucket1 ^ nums[i]
            else: bucket2=bucket2 ^ nums[i]
        return [bucket1,bucket2]
        