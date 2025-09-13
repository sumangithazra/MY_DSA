class Solution:
    def generated_eachRow(self,row):
        temp=[]
        ans=1
        temp.append(1)
        for col in range(1,row):
            ans=ans*(row-col)
            ans=ans//col
            temp.append(ans)
        return temp
    def generate(self, numRows: int) -> List[List[int]]:
        final=[]
        for i in range(1,numRows+1):
            final.append(self.generated_eachRow(i))
        return final

        
        