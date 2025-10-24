class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        dp=[[-1]*n for _ in range(n)]
        for col in range(n):
            dp[0][col]=matrix[0][col]

        for row in range(1,n):
            for col in range(n):
                ld=1e9
                rd=1e9
                up=matrix[row][col]+dp[row-1][col]
                if col-1>=0 : ld=matrix[row][col]+dp[row-1][col-1]
                if col+1<n : rd=matrix[row][col]+dp[row-1][col+1]
                dp[row][col]=min(up,ld,rd)
        mini=dp[n-1][0]
        for col in range(1,n):
            mini=min(mini,dp[n-1][col])
        return mini
        