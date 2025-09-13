class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        suff=1
        pref=1
        maxi=-float('inf')
        for i in range(n):
            if pref==0: pref=1
            if suff==0: suff=1
            pref*=nums[i]
            suff*=nums[n-i-1]
            maxi=max(maxi,max(pref,suff))
        return maxi

        