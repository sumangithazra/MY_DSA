class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st=[]
        leng=len(part)
        n=len(s)
        for i in range(n):
            st.append(s[i])
            if len(st)>=leng and "".join(st[-leng:])==part:
                for i in range(leng):
                    st.pop()
        return "".join(st)
        