class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''left=m-1
        right=0
        while left>=0 and right<n:
            if nums1[left]>nums2[right]:
                nums1[left],nums2[right]=nums2[right],nums1[left]
                left-=1
                right+=1
            else: break
        

        nums1[:m]=sorted(nums1[:m])
        nums2.sort()
        nums1[m:]=nums2'''
        def swap(nums1,nums2,left,right):
            if nums1[left]>nums2[right]:
                nums1[left],nums2[right]=nums2[right],nums1[left]
        length=m+n
        gap=(length//2)+(length%2)
        while gap>0:
            left=0
            right=left+gap
            while right<length:
                if left<m and right>=m:
                    swap(nums1,nums2,left,right-m)
                    left+=1
                    right+=1
                elif left>=m:
                    swap(nums2,nums2,left-m,right-m)
                    left+=1
                    right+=1
                else:
                    swap(nums1,nums1,left,right)
                    left+=1
                    right+=1
            if gap==1: break
            gap=(gap//2)+(gap%2)
        nums1[m:]=nums2                  