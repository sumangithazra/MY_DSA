from collections import Counter
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        dictionary=Counter(nums)
        ans=0
        for num, val in dictionary.items():
            if val==2:
                ans=ans^num
        return ans

        