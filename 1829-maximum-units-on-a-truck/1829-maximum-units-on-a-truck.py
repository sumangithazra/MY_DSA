class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse=True, key=lambda x: x[1])
        total_val=0
        count=0
        for i in range(len(boxTypes)):
            if count+boxTypes[i][0]<=truckSize:
                count+=boxTypes[i][0]
                total_val+=boxTypes[i][0]* boxTypes[i][1]
            else:
                total_val+=(truckSize-count)*boxTypes[i][1]
                break
        return total_val
        