class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cS = 0
        cT = 0
        
        while cS<len(s) and cT < len(t):
            if s[cS] == t[cT]:
                cS+=1
            cT+=1
        
        return cS==len(s)