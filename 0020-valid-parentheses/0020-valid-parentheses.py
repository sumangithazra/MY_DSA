class Solution:
    def isValid(self, s: str) -> bool:
        '''stack=[]
        dic={')':'(','}':'{',']':'['}
        for elem in s:
            if elem in dic:
                top_elem=stack.pop() if stack else "*"
                if dic[elem]!=top_elem:
                    return False
            else:
                stack.append(elem)
        return not stack'''
        dictionary={'(':')','{':'}','[':']'}
        st=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                st.append(i)
            else:
                if not st:return False
                if i!=dictionary[st[-1]]:return False
                else:
                    st.pop()
        if st: return False
        return True       