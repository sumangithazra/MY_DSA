class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''arr=[]
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                arr.append(asteroids[i])
            else:
                while  arr and arr[-1]>0 and arr[-1]<abs(asteroids[i]):
                    arr.pop()
                if  arr and arr[-1]==abs(asteroids[i]):
                    arr.pop()
                elif not arr or arr[-1]<0:
                    arr.append(asteroids[i])
        return arr'''
        st=[]
        n=len(asteroids)
        for i in range(n):
            if asteroids[i]>0: st.append(asteroids[i])
            else:
                while st and st[-1]>0 and st[-1]<abs(asteroids[i]):
                    st.pop()
                if st and st[-1]==abs(asteroids[i]):
                    st.pop()
                elif not st or st[-1]<0:
                    st.append(asteroids[i])
        return st
        