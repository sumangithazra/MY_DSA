class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        count1=0
        count2=0
        elem1=float('inf')
        elem2=float('inf')
        for i in range(n):
            if count1==0 and nums[i]!=elem2:
                count1=1
                elem1=nums[i]
            elif count2==0 and nums[i]!=elem1:
                count2=1
                elem2=nums[i]
            elif nums[i]==elem1: count1+=1
            elif nums[i]==elem2: count2+=1
            else:
                count1-=1
                count2-=1
        count1=0
        count2=0
        mini=n//3 +1
        for i in range(n):
            if nums[i]==elem1: count1+=1
            elif nums[i]==elem2: count2+=1
        result=[]
        if count1 >=mini: result.append(elem1)
        if count2>=mini: result.append(elem2)
        return result

    