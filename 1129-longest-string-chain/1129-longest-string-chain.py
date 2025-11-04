class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n=len(words)
        words.sort(key=len)
        dp=[1]*n
        maxi=1
        def compair(s,t):
            if len(s)!=len(t)+1: return False
            first=0
            second=0
            while first<len(s):
                if second<len(t) and s[first]==t[second]:
                    first+=1
                    second+=1
                else:
                    first+=1
            return second==len(t)
        for idx in range(n):
            for pidx in range(idx):
                if compair(words[idx],words[pidx]) and 1+dp[pidx]>dp[idx]:
                    dp[idx]=1+dp[pidx]
            maxi=max(maxi,dp[idx])
        return maxi

        