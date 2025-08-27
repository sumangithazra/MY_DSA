class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''if len(nums)==0:
            return 0
        longest=1
        nums_set=set(nums)
        current=0
        current_streak=0
        for num in nums_set:
            if num-1  not in nums_set:
                current=num
                current_streak=1
            while current+1 in nums_set:
                current+=1
                current_streak+=1
            longest=max(longest,current_streak)
        return longest'''
        if len(nums)==0: return 0
        longest=1
        temp=set(nums)
        for num in temp:
            if num-1 not in temp:
                count=1
                while num+1 in temp:
                    count+=1
                    num+=1
                longest=max(longest,count)
        return longest

        

        