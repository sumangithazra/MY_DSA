class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])

        def findRow(mat,col):
            idx=-1
            maxi=-1
            for i in range(n):
                if mat[i][mid]>maxi:
                    maxi=mat[i][mid]
                    idx=i
            return idx

        low=0
        high=m-1
        while low<=high:
            mid=low+(high-low)//2
            row=findRow(mat, mid)
            left=mat[row][mid-1] if mid-1>=0 else -1
            right=mat[row][mid+1] if mid+1<m else -1
            if mat[row][mid] >left and mat[row][mid]>right: return [row,mid]
            if mat[row][mid]<left:
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]
