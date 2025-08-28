class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        n=len(intervals)
        count=1
        last_seen=intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]>=last_seen:
                count+=1
                last_seen=intervals[i][1]
        return n-count


        