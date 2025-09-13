class Solution:
    def merge(self,nums,low,mid,high):
        l1=nums[low:mid+1]
        l2=nums[mid+1:high+1]
        n=len(l1)
        m=len(l2)
        left=0
        right=0
        while left <n and right<m:
            if l1[left]<=l2[right]:
                nums[low]=l1[left]
                left+=1
                low+=1
            else:
                nums[low]=l2[right]
                right+=1
                low+=1
        while left<n:
            nums[low]=l1[left]
            left+=1
            low+=1
        while right<m:
            nums[low]=l2[right]
            right+=1
            low+=1
    def count_reverse(self,nums,low,mid,high):
        count=0
        right=mid+1
        for i in range(low,mid+1):
            while right<=high and nums[i]>2*nums[right]:
                right+=1
            count+=(right-(mid+1))
        return count

    def merge_sort(self,nums,low,high):
        count=0
        if low<high:
            mid=low+(high-low)//2
            count=count+self.merge_sort(nums,low,mid)
            count=count+self.merge_sort(nums,mid+1,high)
            count=count+self.count_reverse(nums,low,mid,high)
            self.merge(nums,low,mid,high)
        return count

    def reversePairs(self, nums: List[int]) -> int:
        count=self.merge_sort(nums,0,len(nums)-1)
        return count
        