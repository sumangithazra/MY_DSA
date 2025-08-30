import copy
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n=len(image)
        m=len(image[0])
        new_image=copy.deepcopy(image)
        original=image[sr][sc]
        if original==color: return new_image
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c):
            if new_image[r][c]!=original :
                return
            new_image[r][c]=color
            for dr,dc in direction:
                new_r=r+dr
                new_c=c+dc
                if 0<=new_r<n and 0<=new_c<m : dfs(new_r,new_c)
        dfs(sr,sc)
        return new_image
