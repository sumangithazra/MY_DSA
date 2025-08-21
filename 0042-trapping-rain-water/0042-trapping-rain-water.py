class Solution:
    def trap(self, height: List[int]) -> int:
        '''n=len(height)
        Left_max=0
        Right_max=0
        total=0
        l=0
        r=n-1
        while l<r:
            if height[l]<=height[r]:
                if Left_max>height[l]:
                    total+=Left_max-height[l]
                else:
                    Left_max=height[l]
                l+=1
            else:
                if Right_max>height[r]:
                    total+=Right_max-height[r]
                else:
                    Right_max=height[r]
                r-=1
        return total'''
        n=len(height)
        l_max=0
        r_max=0
        l=0
        r=n-1
        total=0
        for i in range(n):
            if height[l]<=height[r]:
                if l_max>height[l]:
                    total+=l_max-height[l]
                else:
                    l_max=height[l]
                l+=1
            else:
                if r_max>height[r]:
                    total+=r_max-height[r]
                else:
                    r_max=height[r]
                r-=1
        return total

        
        