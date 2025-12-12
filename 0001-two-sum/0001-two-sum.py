class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       number_map={}
       for i, num in enumerate(nums):
        complement=target-num
        if complement in number_map:
            return [number_map[complement],i]
        number_map[num]=i 
        