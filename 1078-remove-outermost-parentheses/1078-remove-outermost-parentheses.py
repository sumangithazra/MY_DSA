class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        '''flag = 0
        output = ""
        for i in s:
            if i=='(':
                if flag>0:
                    output+=i
                flag+=1
            if i==')':
                flag-=1
                if flag>0:
                    output+=i
        return output'''
        ans=""
        count=0
        for i in s:
            if i=='(':
                if count>0:
                    ans+=i
                count+=1
            else:
                count-=1
                if count>0:
                    ans+=i
        return ans
            