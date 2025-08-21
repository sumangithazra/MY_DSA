class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''nge=[]
        stack=[]
        n=len(nums)
        for i in range(2*n-1,-1,-1):
            temp=nums[i%n]
            while stack and stack[-1]<=nums[i % n]:
                stack.pop()
            if i<n:
                if stack:
                    nums[i]=stack[-1]
                else:
                    nums[i]=-1
            stack.append(temp)
        return nums'''
        n=len(nums)
        nge=[0]*n
        st=[]
        for i in range(2*n-1,-1,-1):
            while st and st[-1]<=nums[i%n]:
                st.pop()
            if i<n:
                temp=st[-1] if st else -1
                nge[i]=temp
            st.append(nums[i%n])
        return nge
