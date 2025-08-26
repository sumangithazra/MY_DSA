class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        low=1
        position.sort()
        high=max(position)-min(position)
        while low<=high:
            mid=low+(high-low)//2
            if self.is_possible(position,m,mid)==True:
                low=mid+1
            else:
                high=mid-1
        return high
    def is_possible(self,position,m,mid):
        count=1
        last_occurance=position[0]
        for i in range(1,len(position)):
            if position[i]-last_occurance>=mid:
                count+=1
                last_occurance=position[i]
        if count>=m: return True
        return False
        