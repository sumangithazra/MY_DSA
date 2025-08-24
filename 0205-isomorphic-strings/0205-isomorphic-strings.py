class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''if len(s)!=len(t):
            return False
        s_map={}
        t_map={}
        for i,j in zip(s,t):
            if i in s_map:
                if s_map[i]!=j:
                    return False
            else:
                s_map[i]=j
            if j in t_map:
                if t_map[j]!=i:
                    return False
            else:
                t_map[j]=i
        return True'''
        if len(s)!=len(t): return False
        s_map={}
        t_map={}
        for i,j in zip(s,t):
            if i in s_map:
                if s_map[i]!=j:
                    return False
            else: s_map[i]=j
            if j in t_map:
                if t_map[j]!=i:
                    return False
            else: t_map[j]=i
        return True



        