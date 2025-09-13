class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''col0=1
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    if j!=0:
                        matrix[0][j]=0
                    else:
                        col0=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if matrix[0][0]==0:
            for i in range(1,n):
                matrix[0][i]=0
        if col0==0:
            for j in range(m):
                matrix[j][0]=0'''
        col0=1
        n=len(matrix)
        m=len(matrix[0])
        for row in range(n):
            for col in range(m):
                if matrix[row][col]==0:
                    matrix[row][0]=0
                    if col!=0:
                        matrix[0][col]=0
                    else: col0=0
        for row in range(1,n):
            for col in range(1,m):
                if matrix[row][0]==0 or matrix[0][col]==0:
                    matrix[row][col]=0
        if matrix[0][0]==0:
            for col in range(1,m):
                matrix[0][col]=0
        if col0==0:
            for row in range(n):
                matrix[row][0]=0

